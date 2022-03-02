import kinectandodrive
import time
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.core.window import Window, Animation
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from threading import Thread
from time import sleep
from Email import Email
from pidev.kivy import DPEAButton
from pidev.kivy import ImageButton
# from datetime import datetime
from pidev.kivy.selfupdatinglabel import SelfUpdatingLabel
from pidev.MixPanel import MixPanel

'''
Globals
'''
MAIN_SCREEN_NAME = 'main'
TIMER_SCREEN_NAME = 'TimerScreen'
WAIT_SCREEN_NAME = 'WaitScreen'
SCREEN_MANAGER = ScreenManager()
mail = Email('kineticmaze@gmail.com', 'kineticmaze7266!')
'''
End Globals
'''


class KinectGUI(App):

    def build(self):
        return SCREEN_MANAGER


Window.clearcolor = (.5, .5, .5, 0.1)  # sets the window color to off-teal


class MainScreen(Screen):
    a1 = ObjectProperty(None)
    b1 = ObjectProperty(None)
    c1 = ObjectProperty(None)
    d1 = ObjectProperty(None)
    e1 = ObjectProperty(None)
    f1 = ObjectProperty(None)
    g1 = ObjectProperty(None)
    h1 = ObjectProperty(None)
    i1 = ObjectProperty(None)
    j1 = ObjectProperty(None)
    k1 = ObjectProperty(None)
    l1 = ObjectProperty(None)
    m1 = ObjectProperty(None)
    n1 = ObjectProperty(None)
    o1 = ObjectProperty(None)
    p1 = ObjectProperty(None)
    q1 = ObjectProperty(None)
    r1 = ObjectProperty(None)
    s1 = ObjectProperty(None)
    t1 = ObjectProperty(None)
    u1 = ObjectProperty(None)
    v1 = ObjectProperty(None)
    w1 = ObjectProperty(None)
    x1 = ObjectProperty(None)
    y1 = ObjectProperty(None)
    z1 = ObjectProperty(None)
    space = ObjectProperty(None)
    star = ObjectProperty(None)
    dash = ObjectProperty(None)
    delete = ObjectProperty(None)
    enter = ObjectProperty(None)
    timer = ObjectProperty(None)
    square = ObjectProperty(None)
    name_string = ""



    enter_pressed = False


    def sleep_till_delete(self):
        self.timer.text = "Enter Name"


    def set_ui(self):
        self.timer.text = "Enter Name"
        MainObjectList = [self.q1, self.w1, self.e1, self.r1, self.t1, self.y1, self.u1, self.i1, self.o1, self.p1,
                          self.a1, self.s1, self.d1, self.f1, self.g1, self.h1, self.j1, self.k1, self.l1, self.space,
                          self.z1, self.x1, self.c1, self.v1, self.b1, self.n1, self.m1, self.star, self.dash,
                          self.delete, self.enter]
        x_spacing = .1
        y_spacing = -.15
        x_offset = 0
        y_offset = 0
        button_count = 0
        for btn in MainObjectList:
            btn.pos_hint = {"x": .02 + x_offset, "y": .55 + y_offset}
            button_count += 1
            x_offset += x_spacing
            btn.color = "lightblue"
            if button_count % 10 == 0:
                x_offset = 0
                y_offset += y_spacing

        self.enter.pos_hint = {"x": 0.1, "y": .1}
        Thread(target=self.square_movement).start()
    def key_update(self, button):
        self.name_string += (str(button.text))
        self.profanity_check()

    def delete_key_update(self):
        self.name_string = self.name_string[:-1]
        self.profanity_check()

    def enter_key_update(self):
        self.profanity_check()
        if len(self.name_string) > 1:
            file = open('storage.txt', 'a')
            file.write(self.name_string + "\n")
            file.close()
            self.enter_pressed = True
            self.name_string = ""
            SCREEN_MANAGER.current = WAIT_SCREEN_NAME
        else:
            self.timer.text = 'not a name!'

    def profanity_check(self):
        curse_words = ['kill','kys','poop','pp','penis','kkk','fuck', 'shit', 'kike', 'fag', 'gay', 'cunt', 'bitch', 'whore', 'dick', 'cunt', 'loon', 'ass',
                       'hole', 'piss', 'retard', 'bastard', 'nigg', 'ussy', 'twink', 'chink', 'gypsy', 'nipp', 'agina', 'coon', 'cum', 'ninny', 'jizz', 'anus', 'phal', 'rect', 'rotic', 'beaner',
                       'cracker', 'hard', 'nazi', 'swastika', 'hitler', 'psy']
        for word in curse_words:
            if word in self.name_string:
                self.name_string = ""
                self.timer.text = self.name_string
            else:
                self.timer.text = self.name_string


    def square_movement(self):
        confidence = 0
        MainObjectList = [self.q1, self.w1, self.e1, self.r1, self.t1, self.y1, self.u1, self.i1, self.o1, self.p1,
                          self.a1, self.s1, self.d1, self.f1, self.g1, self.h1, self.j1, self.k1, self.l1, self.space,
                          self.z1, self.x1, self.c1, self.v1, self.b1, self.n1, self.m1, self.star, self.dash,
                          self.delete, self.enter]
        leftlimit = 0
        rightlimit = 0

        x_movement = 14*5.7
        y_movement = 14 * 6.5

        while not self.enter_pressed:
            try:
                sleeptime = 10 / kinectandodrive.close_body.joints[26].position.xyz.z
            except Exception as e:
                sleeptime  = 0.5
                print(e)
            if kinectandodrive.delete:
                confidence += 1
                sleep(0.2)
                if confidence > 4:
                    print('deleting')
                    self.delete_key_update()
                    sleep(0.2)
                    confidence = 0
                kinectandodrive.delete = False
                sleep(0.25)

            if kinectandodrive.rightmove:
                confidence += 1
                sleep(0.1)
                if confidence > 4:
                    ''''''
                    self.square.x += x_movement
                    if self.square.x > 725.824:
                        self.square.x -= x_movement * 10
                        self.square.y -= y_movement
                    if self.square.y < 139:
                        self.square.x = 87.424
                        self.square.y = 48

                    ''''''
                    confidence = 0
                kinectandodrive.rightmove = False
                sleep(sleeptime)

            if kinectandodrive.leftmove:
                confidence += 1
                sleep(0.1)
                if confidence > 4:

                    ''''''
                    self.square.x -= x_movement
                    if self.square.x < 7.6239:
                        self.square.x += x_movement * 10
                        self.square.y += y_movement
                    if self.square.y > 321:
                        self.square.y -= y_movement

                    ''''''
                    confidence = 0
                kinectandodrive.leftmove = False
                sleep(sleeptime)

            if kinectandodrive.click:
                confidence += 1
                sleep(1)
                if confidence > 4:
                    try:
                        print('clicked')
                        for thing in MainObjectList:
                            if self.square.collide_widget(thing):
                                print(thing.text)
                                thing.trigger_action(duration=0.1)
                                thing.color = (1, 1, 1, 0.89)
                                sleep(0.2)
                                thing.color = "lightblue"
                    except Exception as e:
                        print(e, 'in click, not a button')
                    confidence = 0
                kinectandodrive.click = False
                sleep(sleeptime)

            sleep(sleeptime)

        

        
class TimerScreen(Screen):
    timer = ObjectProperty(None)

    def timer_update_thread(self):
        Thread(target=kinectandodrive.start).start()
        Thread(target=self.timer_update).start()

    def timer_update(self):
        self.timer.font_size = 150
        self.timer.text = "GET READY!"
        sleep(2)
        self.timer.text = "THREE"
        sleep(0.8)
        self.timer.text = "TWO"
        sleep(0.8)
        self.timer.text = "ONE"
        sleep(0.8)
        self.timer.text = "GO!!!"
        sleep(0.7)
        init_time = time.time()
        while True:
            seconds = int(time.time() - init_time)
            print(seconds, 'seconds passed')
            print('')
            self.timer.font_size = 400
            self.timer.text = str(seconds)
            sleep(1)
            if not kinectandodrive.KinectIsOn:
                print("Seconds Passed:", seconds)
                file = open('storage.txt', 'a')
                file.write(str(seconds) + ' ')
                file.close()
                SCREEN_MANAGER.current = MAIN_SCREEN_NAME
                break



class WaitScreen(Screen):

    first_place = ObjectProperty(None)
    loading = ObjectProperty(None)

    currentscore = ObjectProperty(None)
    print("Before file")

    # lines = []
    # scores = []
    # names = []


    def score_update(self):
        global pairsList

        with open('storage.txt', 'r') as f:
            last_line = f.readlines()[-1]
            placeholder = "Your score: "+ str(last_line.split()[0]) + " seconds"
            self.currentscore.text = placeholder

        scores = []
        names = []
        with open("storage.txt", "r") as file:
            for line in file:
                split_line = line.strip().split()
                scores.append(split_line[0])
                names.append(split_line[1])
        print("Scores:", scores)
        print("Names:", names)

        pairs = list(zip(scores, names))
        print("Pairs Before:", pairs)
        pairs.sort(key=lambda pair: int(pair[0]))
        print("Pairs After:", pairs)
        pairsList = dict(pairs)
        mail.checkForEmailConstantly(target_body="scores", response_body=str(pairsList),
                                     response_subject="Hello from the Kinetic Maze! Here are your top scores: ")
        # I think it stopped working

        count = 0
        score_board = ""
        while count < 10:
            score_board += pairs[count][0] + " " + pairs[count][1] + "\n"
            count += 1
        self.first_place.text = score_board

        Thread(target=self.switch_screen).start()

    def switch_screen(self):
        sleep(7)
        kinectandodrive.KinectIsOn = True
        SCREEN_MANAGER.current = TIMER_SCREEN_NAME


Builder.load_file('TimerScreen.kv')
Builder.load_file('main.kv')
Builder.load_file('WaitScreen.kv')

SCREEN_MANAGER.add_widget(TimerScreen(name=TIMER_SCREEN_NAME))
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))
SCREEN_MANAGER.add_widget(WaitScreen(name=WAIT_SCREEN_NAME))


if __name__ == '__main__':
    KinectGUI().run()
