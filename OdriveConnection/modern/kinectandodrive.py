from ODrive_Ease_Lib import *
import random
import sys
import time
from threading import Thread
from time import sleep
import atexit
import cv2
import numpy as np
from pykinect_azure.k4abt._k4abtTypes import K4ABT_JOINT_NAMES

sys.path.insert(1, '../../')
import pykinect_azure as pykinect
from pykinect_azure.k4a import _k4a
from pykinect_azure.k4abt import _k4abt

'''
Globals
'''
# odrive
odboard = odrive.find_any(serial_number='208D3388304B')
ax = ODrive_Axis(odboard.axis0, 15, 10)  # current, velocity limits
ay = ODrive_Axis(odboard.axis1, 40, 16)  # current, velocity limits
odboard.clear_errors()
# kinect
close_body = None
KinectIsOn = True
takeheadz = "100"
# keyboard
leftmove = False
rightmove = False
click = False
delete = False
'''
End Globals
'''


def reset_global_variables():
    global close_body, click, KinectIsOn, leftmove, rightmove, delete
    close_body = None
    KinectIsOn = True
    leftmove = False
    click = False
    rightmove = False
    delete = False

    takeheadz = "100"


def odrive_setup():
    dump_errors(odboard)
    if not ax.is_calibrated():
        print("calibrating x...")
        ax.calibrate_with_current_lim(25)

    ax.gainz(20, 0.16, 0.32, False)
    odboard.clear_errors()

    ax.idle()
    ay.idle()
    proximity_setup(ax, 2)
    proximity_setup(ay, 8)
    # Firmata setup
        # SCREEN_MANAGER = ScreenManager()
        # MAIN_SCREEN_NAME = 'main'
        # board = Arduino("/dev/ttyACM1")
        # # Change to your port
        # from time import sleep
        # class ProjectNameGUI(App):
        #     tester = ObjectProperty(DPEAButton)
        #
        #     def build(self):
        #         """
        #         Build the application
        #         :return: Kivy Screen Manager instance
        #         """
        #         return SCREEN_MANAGER
        #
        # class MainScreen(Screen):
        #     xcv = 0
        #
        #     def switch(self):
        #         if self.xcv == 1:
        #             board.digital[13].write(0)
        #             self.xcv = 0
        #             print(self.xcv)
        #         elif self.xcv == 0:
        #             board.digital[13].write(1)
        #             self.xcv = 1
        #             print(self.xcv)


def proximity_setup(axys, num):
    axisshortcut = axys.axis
    # homing_sensor_prox
    odboard.config.gpio8_mode = GPIO_MODE_DIGITAL
    axisshortcut.min_endstop.config.gpio_num = num  # pin 8 for x, 2 for y, 2 for z
    Prox_Sensor_Number = axisshortcut.min_endstop.config.gpio_num  # setting to global class Runner variable just so that I can reference it in the Thread print statements
    axisshortcut.min_endstop.config.enabled = True  # Turns sensor on, says that I am using it
    axisshortcut.min_endstop.config.offset = 1  # stops 1 rotation away from sensor
    axisshortcut.min_endstop.config.debounce_ms = 20  # checks again after 20 milliseconds if actually pressed, which is what debounce is :D
    axisshortcut.min_endstop.config.offset = -1.0 * (8192)  # hop back from GPIO in order to allow for function again
    odboard.config.gpio8_mode = GPIO_MODE_DIGITAL_PULL_DOWN

    # print(Prox_Sensor_Number)

    sleep(1)


def search_for_closest_body(frame):
    global close_body
    body_list = [frame.get_body_skeleton(body_num) for body_num in
                 range(frame.get_num_bodies())]  # creates bodylist
    try:
        close_body = min(body_list, key=lambda body: body.joints[
            26].position.xyz.z)  # grabs the minimum body according to the head z depth
    except ValueError:
        close_body = None


def check_prox_sensor(axis, ret=False):
    if axis.axis.min_endstop.endstop_state:  # if switch, or in this case the prox is pressed
        # dump_errors(odboard)
        odboard.clear_errors()
        ax.set_vel(0)
        if ret:
            return True
        else:
            print('Reached Prox on GPIO', axis.axis.min_endstop.config.gpio_num)


def kinect_start():
    global KinectIsOn
    reset_global_variables()
    # Initialize the library, if the library is not found, add the library path as argument
    pykinect.initialize_libraries(module_k4abt_path="/usr/lib/libk4abt.so", track_body=True)

    device_config = pykinect.default_configuration
    device_config.color_resolution = pykinect.K4A_COLOR_RESOLUTION_OFF
    device_config.depth_mode = pykinect.K4A_DEPTH_MODE_WFOV_2X2BINNED

    device = pykinect.start_device(config=device_config)

    bodyTracker = pykinect.start_body_tracker()

    cv2.namedWindow('Depth image with skeleton', cv2.WINDOW_NORMAL)

    while True:

        capture = device.update()

        body_frame = bodyTracker.update()

        ret, depth_color_image = capture.get_colored_depth_image()

        ret, body_image_color = body_frame.get_segmentation_image()

        if not ret:
            continue

        combined_image = cv2.addWeighted(depth_color_image, 0.6, body_image_color, 0.4, 0)

        combined_image = body_frame.draw_bodies(combined_image)

        cv2.imshow('Depth image with skeleton', combined_image)

        if cv2.waitKey(1) == ord('q'):
            break

        search_for_closest_body(body_frame)
        check_prox_sensor(ay)
        check_prox_sensor(ax)


        try:

            global pelvisx, pelvisy, pelvisz, spine_navelx, spine_navely, spine_navelz, spine_chestx, spine_chesty, \
                spine_chestz, neckx, necky, neckz, clavicle_leftx, clavicle_lefty, clavicle_leftz, shoulder_leftx, \
                shoulder_lefty, shoulder_leftz, elbow_leftx, elbow_lefty, elbow_leftz, wrist_leftx, wrist_lefty, wrist_leftz, \
                hand_leftx, hand_lefty, hand_leftz, handtip_leftx, handtip_lefty, handtip_leftz, thumb_leftx, thumb_lefty, thumb_leftz, \
                clavicle_rightx, clavicle_righty, clavicle_rightz, shoulder_rightx, shoulder_righty, shoulder_rightz, elbow_rightx, elbow_righty, \
                elbow_rightz, wrist_rightx, wrist_righty, wrist_rightz, hand_rightx, hand_righty, hand_rightz, handtip_rightx, handtip_righty, handtip_rightz, \
                thumb_rightx, thumb_righty, thumb_rightz, hip_leftx, hip_lefty, hip_leftz, knee_leftx, knee_lefty, knee_leftz, ankle_leftx, ankle_lefty, ankle_leftz, \
                foot_leftx, foot_lefty, foot_leftz, hip_rightx, hip_righty, hip_rightz, knee_rightx, knee_righty, knee_rightz, ankle_rightx, ankle_righty, ankle_rightz, \
                foot_rightx, foot_righty, foot_rightz, headx, heady, headz, nosex, nosey, nosez, eye_leftx, eye_lefty, eye_leftz, \
                handslope

            pelvisx = close_body.joints[0].position.xyz.x
            pelvisy = close_body.joints[0].position.xyz.y
            pelvisz = close_body.joints[0].position.xyz.z
            spine_navelx = close_body.joints[1].position.xyz.x
            spine_navely = close_body.joints[1].position.xyz.y
            spine_navelz = close_body.joints[1].position.xyz.z
            spine_chestx = close_body.joints[2].position.xyz.x
            spine_chesty = close_body.joints[2].position.xyz.y
            spine_chestz = close_body.joints[2].position.xyz.z
            neckx = close_body.joints[3].position.xyz.x
            necky = close_body.joints[3].position.xyz.y
            neckz = close_body.joints[3].position.xyz.z
            clavicle_leftx = close_body.joints[4].position.xyz.x
            clavicle_lefty = close_body.joints[4].position.xyz.y
            clavicle_leftz = close_body.joints[4].position.xyz.z
            shoulder_leftx = close_body.joints[5].position.xyz.x
            shoulder_lefty = close_body.joints[5].position.xyz.y
            shoulder_leftz = close_body.joints[5].position.xyz.z
            elbow_leftx = close_body.joints[6].position.xyz.x
            elbow_lefty = close_body.joints[6].position.xyz.y
            elbow_leftz = close_body.joints[6].position.xyz.z
            wrist_leftx = close_body.joints[7].position.xyz.x
            wrist_lefty = close_body.joints[7].position.xyz.y
            wrist_leftz = close_body.joints[7].position.xyz.z
            hand_leftx = close_body.joints[8].position.xyz.x
            hand_lefty = close_body.joints[8].position.xyz.y
            hand_leftz = close_body.joints[8].position.xyz.z
            handtip_leftx = close_body.joints[9].position.xyz.x
            handtip_lefty = close_body.joints[9].position.xyz.y
            handtip_leftz = close_body.joints[9].position.xyz.z
            thumb_leftx = close_body.joints[10].position.xyz.x
            thumb_lefty = close_body.joints[10].position.xyz.y
            thumb_leftz = close_body.joints[10].position.xyz.z
            clavicle_rightx = close_body.joints[11].position.xyz.x
            clavicle_righty = close_body.joints[11].position.xyz.y
            clavicle_rightz = close_body.joints[11].position.xyz.z
            shoulder_rightx = close_body.joints[12].position.xyz.x
            shoulder_righty = close_body.joints[12].position.xyz.y
            shoulder_rightz = close_body.joints[12].position.xyz.z
            elbow_rightx = close_body.joints[13].position.xyz.x
            elbow_righty = close_body.joints[13].position.xyz.y
            elbow_rightz = close_body.joints[13].position.xyz.z
            wrist_rightx = close_body.joints[14].position.xyz.x
            wrist_righty = close_body.joints[14].position.xyz.y
            wrist_rightz = close_body.joints[14].position.xyz.z
            hand_rightx = close_body.joints[15].position.xyz.x
            hand_righty = close_body.joints[15].position.xyz.y
            hand_rightz = close_body.joints[15].position.xyz.z
            handtip_rightx = close_body.joints[16].position.xyz.x
            handtip_righty = close_body.joints[16].position.xyz.y
            handtip_rightz = close_body.joints[16].position.xyz.z
            thumb_rightx = close_body.joints[17].position.xyz.x
            thumb_righty = close_body.joints[17].position.xyz.y
            thumb_rightz = close_body.joints[17].position.xyz.z
            hip_leftx = close_body.joints[18].position.xyz.x
            hip_lefty = close_body.joints[18].position.xyz.y
            hip_leftz = close_body.joints[18].position.xyz.z
            knee_leftx = close_body.joints[19].position.xyz.x
            knee_lefty = close_body.joints[19].position.xyz.y
            knee_leftz = close_body.joints[19].position.xyz.z
            ankle_leftx = close_body.joints[20].position.xyz.x
            ankle_lefty = close_body.joints[20].position.xyz.y
            ankle_leftz = close_body.joints[20].position.xyz.z
            foot_leftx = close_body.joints[21].position.xyz.x
            foot_lefty = close_body.joints[21].position.xyz.y
            foot_leftz = close_body.joints[21].position.xyz.z
            hip_rightx = close_body.joints[22].position.xyz.x
            hip_righty = close_body.joints[22].position.xyz.y
            hip_rightz = close_body.joints[22].position.xyz.z
            knee_rightx = close_body.joints[23].position.xyz.x
            knee_righty = close_body.joints[23].position.xyz.y
            knee_rightz = close_body.joints[23].position.xyz.z
            ankle_rightx = close_body.joints[24].position.xyz.x
            ankle_righty = close_body.joints[24].position.xyz.y
            ankle_rightz = close_body.joints[24].position.xyz.z
            foot_rightx = close_body.joints[25].position.xyz.x
            foot_righty = close_body.joints[25].position.xyz.y
            foot_rightz = close_body.joints[25].position.xyz.z
            headx = close_body.joints[26].position.xyz.x
            heady = close_body.joints[26].position.xyz.y
            headz = close_body.joints[26].position.xyz.z
            nosex = close_body.joints[27].position.xyz.x
            nosey = close_body.joints[27].position.xyz.y
            nosez = close_body.joints[27].position.xyz.z
            eye_leftx = close_body.joints[28].position.xyz.x
            eye_lefty = close_body.joints[28].position.xyz.y
            eye_leftz = close_body.joints[28].position.xyz.z

            handslope = (hand_lefty - hand_righty) / (hand_leftx - hand_rightx)

        except Exception as e:
            pass
            # print('no body found', e)
        if close_body is not None and KinectIsOn:

            if -0.2 < handslope < 0.2:
                ax.set_vel(0)
            if handslope > 0.2:
                ax.set_vel(-4)
            if handslope < -0.2:
                ax.set_vel(4)

            if hand_rightx < -700 or hand_rightx > 700:
                ax.set_vel(0)

            if hand_leftx < -700 or hand_leftx > 700:
                ax.set_vel(0)

        if check_prox_sensor(ax, True) or check_prox_sensor(ay, True):
            ax.set_vel(0)
            KinectIsOn = False


        elif close_body is not None and not KinectIsOn:
            global takeheadz
            takeheadz = 100

            tolerance = 100

            if (heady + tolerance) > hand_lefty > (heady - tolerance) and (
                    headx + tolerance) > hand_leftx > (headx - tolerance) or (
                    heady + tolerance) > hand_righty > (heady - tolerance) and (
                    headx + tolerance) > hand_rightx > (headx - tolerance):
                global click
                click = True

            elif hand_leftx - hand_rightx < tolerance and hand_rightx - hand_leftx < tolerance and hand_righty - hand_lefty < tolerance:  # Put ya hands together y'all!
                global downmove
                # downmove = True

            elif handslope > 0.2:
                global leftmove
                takeheadz = headz
                leftmove = True

            elif handslope < -0.2:
                global rightmove

                takeheadz = headz
                rightmove = True

            elif hand_rightz > headz + tolerance and hand_leftz > headz + tolerance:
                global delete
                delete = True

            # elif hand_rightx < -700 or hand_rightx > 700:
            #     ax.set_vel(0)
            #
            # elif hand_leftx < -700 or hand_leftx > 700:
            #     ax.set_vel(0)

            if -0.2 < handslope < 0.2:
                global level
                level = True

        if close_body == None:
            ax.set_vel(0)

def start():
    odrive_setup()
    kinect_start()

def restart():
    Thread(target=kinect_start).start()


if __name__ == '__main__':
    start()