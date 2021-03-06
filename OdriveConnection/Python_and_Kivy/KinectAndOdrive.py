# This is a sample Python script.
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from threading import Thread
from time import sleep
import time
from odrive.enums import *  # enumerations, enums, gives each sensor numbers
import odrive
# buttons are actually buttons -1
# from pidev.Joystick import Joystick
from ODrive_Ease_Lib import *

#EMAIL< IFBREAKCODE< DELETETHIS

from EmailModule import checkforEmail
# import main#never do this!?
# variables
# findodrive
odboard = odrive.find_any(serial_number='208D3388304B')
odboard.clear_errors()
odboard1 = odrive.find_any(serial_number='2065339E304B')
odboard1.clear_errors()
# setup the Kinect

# file = open("logging.txt","r+")
# file.truncate(0)
# file.close()
#
# def fileappend(target):
#     with open("logging.txt", 'a') as f:
#         f.write(target+"\n")

import random
import sys
import time
#comm localhost email status
import atexit

import cv2
from pykinect_azure.k4abt._k4abtTypes import K4ABT_JOINT_NAMES

sys.path.insert(1, '../../')
import pykinect_azure as pykinect
from pykinect_azure.k4a import _k4a
from pykinect_azure.k4abt import _k4abt

# Kivy Imports


from threading import Thread
from time import sleep

# from datetime import datetime
import pyautogui

# time = datetime

#types.apppend me4thod options

# def uniqueAddStatus(target, array):#array: list):#zeyn helped types use colon for type: only in funtions like this or methods #thisisdead
#     tempstr = array[-1]
#     if str(target) == tempstr.lower():
#         pass
#     else:
#         print(target, "added")
#         array.append(target)


KinectIsOn = True
kivyIsOn = False
time_start = time.time()
KeyboardIsOn = False

click = False
rightmove = False
leftmove = False
upmove = False
downmove = False
enter = False
middle = False
delete = False
level = False
takeheadz = 1400


def global_variable_reset():
    global KinectIsOn
    global kivyIsOn
    global time_start
    global TimerRunning
    global seconds
    global KeyboardIsOn
    KeyboardIsOn = False
    KinectIsOn = True
    kivyIsOn = False
    time_start = time.time()

    # timer_update()

# def timer_update():
#     global seconds
#     global TimerRunning
#     while TimerRunning:
#         # print ("Timer On")
#         print(seconds)
#         print(' ')
#         print(' ')
#         time.sleep(1)
#         seconds = int(time.time() - time_start)


# def Kivy_Update():
#
#     print("Seconds Passed:", seconds)
#     file = open('storage.txt', 'a')
#     file.write('\n'+str(seconds) + '')
#     file.close()
#     global TimerRunning
#     TimerRunning = False


# https://stackoverflow.com/questions/56711424/how-can-i-count-time-in-python-3


def odrive_and_kinect_startup():
    counter = 0
    counter1 = 0
    global KinectIsOn
    KinectIsOn = True
    global KeyboardIsOn
    # KeyboardIsOn = False
    # dumperrors
    dump_errors(odboard)
    # define ax and ay
    ax = ODrive_Axis(odboard.axis0, 15, 10)  # currentlim, vlim
    ay = ODrive_Axis(odboard.axis1, 40, 16)  # currentlim, vlim
    az = ODrive_Axis(odboard1.axis0, 15, 10)
    # calibrate
    if not ax.is_calibrated():  # calibrate x (left right)
        print("calibrating x...")
        ax.calibrate_with_current_lim(25)

    if not az.is_calibrated():  # calibrate z (left right)
        print("calibrating z...")
        az.calibrate_with_current_lim(25)


    ax.gainz(20, 0.16, 0.32, False)
    az.gainz(20, 0.16, 0.32, False)
    odboard.clear_errors()

    ax.idle()
    ay.idle()
    az.idle()
    axisshortcut = az.axis
    # homing_sensor_prox
    odboard1.config.gpio8_mode = GPIO_MODE_DIGITAL
    axisshortcut.min_endstop.config.gpio_num = 2  # pin 8 for x, 2 for y, 2 for z
    Prox_Sensor_Number = axisshortcut.min_endstop.config.gpio_num  # setting to global class Runner variable just so that I can reference it in the Thread print statements
    axisshortcut.min_endstop.config.enabled = True  # Turns sensor on, says that I am using it
    axisshortcut.min_endstop.config.offset = 1  # stops 1 rotation away from sensor
    axisshortcut.min_endstop.config.debounce_ms = 20  # checks again after 20 milliseconds if actually pressed, which is what debounce is :D
    axisshortcut.min_endstop.config.offset = -1.0 * (8192)  # hop back from GPIO in order to allow for function again
    odboard1.config.gpio8_mode = GPIO_MODE_DIGITAL_PULL_DOWN

    sleep(5)

    # initilize the Kinect

    # Initialize the library, if the library is not found, add the library path as argument
    pykinect.initialize_libraries(module_k4abt_path="/usr/lib/libk4abt.so", track_body=True)

    # Modify camera configuration
    device_config = pykinect.default_configuration
    device_config.color_resolution = pykinect.K4A_COLOR_RESOLUTION_OFF
    device_config.depth_mode = pykinect.K4A_DEPTH_MODE_WFOV_2X2BINNED
    # print(device_config)

    # Start device
    device = pykinect.start_device(config=device_config)


    # Start body tracker
    bodyTracker = pykinect.start_body_tracker()

#finaldellater
    cv2.namedWindow('Depth image with skeleton', cv2.WINDOW_NORMAL)#hastagoutiferroring


#del

    # run the Kinect
    capture_list = []

    # START TIM
    # Thread(target=timer_update).start()

    while True:

        # Get capture
        capture = device.update()

        # Get body tracker frame
        body_frame = bodyTracker.update()  # LOOK HERE

#finaldelete


        # Get the color depth image from the capture
        ret, depth_color_image = capture.get_colored_depth_image()

        # Get the colored body segmentation
        ret, body_image_color = body_frame.get_segmentation_image()

        if not ret:
            continue

        # Combine both images
        combined_image = cv2.addWeighted(depth_color_image, 0.6, body_image_color, 0.4, 0)

        # Draw the skeletons
        combined_image = body_frame.draw_bodies(combined_image) # LOOK HERE

        # Overlay body segmentation on depth image
        cv2.imshow('Depth image with skeleton',combined_image)



#del




        if KinectIsOn:
            body_list = [body_frame.get_body_skeleton(body_num) for body_num in
                         range(body_frame.get_num_bodies())]  # le code
            try:
                close_body = min(body_list, key=lambda body: body.joints[
                    26].position.xyz.z)  # grabs the minimum body according to the head z depth
            except ValueError:
                close_body = None

            if close_body != None:
                rightz = close_body.joints[15].position.xyz.z
                leftz = close_body.joints[8].position.xyz.z

                righthand = close_body.joints[15].position.xyz.x
                lefthand = close_body.joints[8].position.xyz.x

                righthandy = close_body.joints[15].position.xyz.y
                lefthandy = close_body.joints[8].position.xyz.y

                shoulderleftx = close_body.joints[5].position.xyz.x
                shoulderlefty = close_body.joints[5].position.xyz.y

                shoulderrightx = close_body.joints[12].position.xyz.x
                shoulderrighty = close_body.joints[12].position.xyz.y

                handslope = (lefthandy - righthandy) / (lefthand - righthand)

                #printing sloep

#                 leftshoulderslope = (lefthandy-shoulderlefty)/(lefthand-shoulderleftx)
#                 rightshoulderslope = (righthandy - shoulderrighty) / (righthand - shoulderrightx)
#                 print(leftshoulderslope, rightshoulderslope)
# #goldencode
#                 if leftshoulderslope > 0.8: #or rightshoulderslope > 0.65:
#                      ax.set_vel(-3)
#                 #
#                 if leftshoulderslope < -0.3: #or rightshoulderslope < -1.5:
#                      ax.set_vel(3)
#
#                 if rightshoulderslope > 0.23:
#                     ax.set_vel(-3)
#
#                 if rightshoulderslope < -1.2:
#                     ax.set_vel(3)
#
#                 if -1.2 < rightshoulderslope < 0.23 and -0.3 < leftshoulderslope < 0.8:
#                     ax.set_vel(0)

                if -0.2 < handslope < 0.2:
                    ax.set_vel(0)
                if handslope > 0.2:
                    ax.set_vel(-3)
                if handslope < -0.2:
                    ax.set_vel(3)

                if righthand < -700 or righthand > 700:
                    ax.set_vel(0)

                if lefthand < -700 or lefthand > 700:
                    ax.set_vel(0)


              #  if rightshoulderslope < 1.5 and leftshoulderslope < 0.08:
                    #ax.set_vel(0)

                # if leftshoulderslope < 0.9 and leftshoulderslope > 0.08:
                #     ax.set_vel(0)
                #
                # if rightshoulderslope < 0.65 and rightshoulderslope > -1.5:
                #     ax.set_vel(0)

            if cv2.waitKey(1) == ord('q'):
                ax.set_vel(0)
                ax.idle()
                break

                # append the images to the array. if the array is == 3000, then run a whilie loop that clear the array according the handle's id.

            if az.axis.min_endstop.endstop_state:  # if switch, or in this case the prox is pressed
                # clear errors will get rid of freeze man
                print('Reached Prox on GPIO', Prox_Sensor_Number)
                dump_errors(odboard1)
                odboard1.clear_errors()
                ax.set_vel(0)
                az.set_vel(0)
                # sleep(3)
                # Thread(target=Kivy_Update).start()
                # sleep(1)
                KinectIsOn = False

        if KeyboardIsOn:

            body_list = [body_frame.get_body_skeleton(body_num) for body_num in
                         range(body_frame.get_num_bodies())]  # creates bodylist
            try:
                close_body = min(body_list, key=lambda body: body.joints[
                    26].position.xyz.z)  # grabs the minimum body according to the head z depth
            except ValueError:
                close_body = None

            if close_body != None:
                headz = close_body.joints[26].position.xyz.z

                headx = close_body.joints[26].position.xyz.x
                heady = close_body.joints[26].position.xyz.y



                righthandx = close_body.joints[15].position.xyz.x
                righthandy = close_body.joints[15].position.xyz.y


                lefthandy = close_body.joints[8].position.xyz.y
                lefthandx = close_body.joints[8].position.xyz.x

                rightz = close_body.joints[15].position.xyz.z
                leftz = close_body.joints[8].position.xyz.z

                righthand = close_body.joints[15].position.xyz.x
                lefthand = close_body.joints[8].position.xyz.x

                righthandy = close_body.joints[15].position.xyz.y
                lefthandy = close_body.joints[8].position.xyz.y

                shoulderleftx = close_body.joints[5].position.xyz.x
                shoulderlefty = close_body.joints[5].position.xyz.y

                shoulderrightx = close_body.joints[12].position.xyz.x
                shoulderrighty = close_body.joints[12].position.xyz.y

                leftelbowx = close_body.joints[6].position.xyz.x
                leftelbowy = close_body.joints[6].position.xyz.y

                rightelbowx = close_body.joints[6].position.xyz.x
                rightelbowy = close_body.joints[6].position.xyz.y

                pelvisx = close_body.joints[0].position.xyz.x
                pelvisy = close_body.joints[0].position.xyz.y

                kneelefty = close_body.joints[19].position.xyz.y

                betweenpelvisandkneesy = (pelvisy + kneelefty) / 2

                rightankley = close_body.joints[24].position.xyz.y


                #printing sloep

                handslope = (lefthandy-righthandy)/(lefthandx-righthandx)

                leftshoulderslope = (lefthandy-shoulderlefty)/(lefthand-shoulderleftx)
                rightshoulderslope = (righthandy - shoulderrighty) / (righthand - shoulderrightx)

                tolerance = 100
                toleranceleftright = 50

                leftheadslope = (lefthandy - heady) / (lefthand - headx)
                rightheadslope = (righthandy - heady) / (righthand - headx)
                # BEHOLD THE FINAL IF STATEMENT#clicking
                # print(headz)
                global takeheadz
                # print(takeheadz)

                if lefthandy < (heady + tolerance) and lefthandy > (heady - tolerance) and lefthandx < (
                        headx + tolerance) and lefthandx > (headx - tolerance) or righthandy < (
                        heady + tolerance) and righthandy > (heady - tolerance) and righthandx < (
                        headx + tolerance) and righthandx > (headx - tolerance):
                    global click
                    click = True




                elif lefthandx - righthandx < tolerance and righthandx - lefthandx < tolerance and righthandy - lefthandy < tolerance:  # Put ya hands together y'all!
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

                elif rightz > headz + tolerance and leftz > headz + tolerance:
                    global delete
                    delete = True


                elif righthand < -700 or righthand > 700:
                    ax.set_vel(0)

                elif lefthand < -700 or lefthand > 700:
                    ax.set_vel(0)

                if -0.2 < handslope < 0.2:
                    # global middle
                    # middle = True
                    # global level
                    # level = True
                    pass

                # print(rightheadslopez)



                # if -0.14 < leftheadslope < .25:
                #     global leftmove
                #     leftmove = True
                #
                # if -0.32 < rightheadslope < .12:
                #     global rightmove
                #     rightmove = True
                #
                #
                # # The bleh code
                #
                # if leftheadslope <= -0.8 and rightheadslope >= 0.8:
                #     global upmove
                #     upmove = True
                #
                # if leftheadslope >= 1.7 and rightheadslope <= -1.7:
                #     global downmove
                #     downmove = True


            if cv2.waitKey(1) == ord('q'):
                ax.set_vel(0)
                ax.idle()
                break


        if KinectIsOn:
            KeyboardIsOn = False
        if KinectIsOn == False:
            KeyboardIsOn = True
        if KeyboardIsOn:
            KinectIsOn = False
        if KeyboardIsOn == False:
            KinectIsOn = True
        # print(KinectIsOn)
        # print((KeyboardIsOn))

        # _k4a.k4a_capture_release(capture.handle())
        # _k4abt.k4abt_frame_release(body_frame.handle())


#
# if __name__ == '__main__':
#
#     # dumperrors
#     dump_errors(odboard)
#     # define ax and ay
#     ax = ODrive_Axis(odboard.axis0, 15, 10)  # currentlim, vlim
#     ay = ODrive_Axis(odboard.axis1, 40, 16)  # currentlim, vlim
#     az = ODrive_Axis(odboard1.axis0, 15, 10)
#     # calibrate
#     if not ax.is_calibrated():  # calibrate x (left right)
#         print("calibrating x...")
#         ax.calibrate_with_current_lim(25)
#     if not az.is_calibrated():  # calibrate z (left right)
#         print("calibrating z...")
#         az.calibrate_with_current_lim(25)
#
#     ax.gainz(20, 0.16, 0.32, False)
#     az.gainz(20, 0.16, 0.32, False)
#     odboard.clear_errors()
#
#     ax.idle()
#     ay.idle()
#     az.idle()
#     axisshortcut = az.axis
#     # homing_sensor_prox
#     odboard1.config.gpio8_mode = GPIO_MODE_DIGITAL
#     axisshortcut.min_endstop.config.gpio_num = 2  # pin 8 for x, 2 for y, 2 for z
#     Prox_Sensor_Number = axisshortcut.min_endstop.config.gpio_num  # setting to global class Runner variable just so that I can reference it in the Thread print statements
#     axisshortcut.min_endstop.config.enabled = True  # Turns sensor on, says that I am using it
#     axisshortcut.min_endstop.config.offset = 1  # stops 1 rotation away from sensor
#     axisshortcut.min_endstop.config.debounce_ms = 20  # checks again after 20 milliseconds if actually pressed, which is what debounce is :D
#     axisshortcut.min_endstop.config.offset = -1.0 * (
#         8192)  # hop back from GPIO in order to allow for function again
#     odboard1.config.gpio8_mode = GPIO_MODE_DIGITAL_PULL_DOWN
#
#     sleep(10)
#
#     # initilize the Kinect
#
#     # Initialize the library, if the library is not found, add the library path as argument
#     pykinect.initialize_libraries(module_k4abt_path="/usr/lib/libk4abt.so", track_body=True)
#
#     # Modify camera configuration
#     device_config = pykinect.default_configuration
#     device_config.color_resolution = pykinect.K4A_COLOR_RESOLUTION_OFF
#     device_config.depth_mode = pykinect.K4A_DEPTH_MODE_WFOV_2X2BINNED
#     # print(device_config)
#
#     # Start device
#     device = pykinect.start_device(config=device_config)
#
#     # Start body tracker
#     bodyTracker = pykinect.start_body_tracker()
#
#     # cv2.namedWindow('Depth image with skeleton', cv2.WINDOW_NORMAL)
#     # run the Kinect
#     capture_list = []
#
#     # Thread(target=timer_update).start()  # START TIM
#
#     while True:
#
#         # Get capture
#         capture = device.update()
#
#         # Get body tracker frame
#         body_frame = bodyTracker.update()  # LOOK HERE
#
#         if KinectIsOn:
#
#             body_list = [body_frame.get_body_skeleton(body_num) for body_num in
#                          range(body_frame.get_num_bodies())]  # le code
#             try:
#                 close_body = min(body_list, key=lambda body: body.joints[
#                     26].position.xyz.z)  # grabs the minimum body according to the head z depth
#             except ValueError:
#                 close_body = None
#
#             if close_body != None:
#                 rightz = close_body.joints[15].position.xyz.z
#                 leftz = close_body.joints[8].position.xyz.z
#
#                 righthand = close_body.joints[15].position.xyz.x
#                 lefthand = close_body.joints[8].position.xyz.x
#
#                 righthandy = close_body.joints[15].position.xyz.y
#                 lefthandy = close_body.joints[8].position.xyz.y
#
#                 if lefthandy < -400 and righthandy > -100:
#                     print("to the LEFT!")
#                     ax.set_vel(3)
#
#                 if lefthandy > -100 and righthandy < -400:
#                     print("to the RIGHT!")
#                     ax.set_vel(-3)
#
#                 if -400 < lefthandy < -100 and -400 < righthandy < -100:
#                     print("in the MIDDLE!")
#                     ax.set_vel(0)
#                     ay.set_vel(0)
#                     # stop if leave the frame
#                 if righthand < -700 or righthand > 700:
#                     print("Stopping because righthand left the frame")
#                     ax.set_vel(0)
#
#                 if lefthand < -700 or lefthand > 700:
#                     print("Stopping because lefthand left the frame")
#                     ax.set_vel(0)
#
#                 print("RightZ:", rightz)
#                 print("LeftY:", lefthandy)
#                 print("RightY:", righthandy)
#
#             # _k4a.k4a_capture_release(capture.handle())
#             # _k4abt.k4abt_frame_release(body_frame.handle())
#
#             if cv2.waitKey(1) == ord('q'):
#                 ax.set_vel(0)
#                 ax.idle()
#                 break
#
#                 # append the images to the array. if the array is == 3000, then run a whilie loop that clear the array according the handle's id.
#
#             if az.axis.min_endstop.endstop_state:  # if switch, or in this case the prox is pressed
#                 # clear errors will get rid of freeze man
#                 print('Reached Prox on GPIO', Prox_Sensor_Number)
#                 dump_errors(odboard1)
#                 odboard1.clear_errors()
#                 sleep(3)
#                 #Thread(target=Kivy_Update).start()
#                 sleep(1)
#                 KinectIsOn = False

# odrv0 208D3388304B
# odrv1 2065339E304B


# Odrv1 = odrive.find_any(serial_number=serial1)
# Odrv2 = odrive.find_any(serial_number=serial2)
