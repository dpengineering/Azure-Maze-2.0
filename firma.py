from pyfirmata import Arduino, util
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

from kivy.uix.button import Button
from pidev.kivy import DPEAButton
from kivy.uix.screenmanager import ScreenManager, Screen

SCREEN_MANAGER= ScreenManager()
MAIN_SCREEN_NAME = 'main'
board = Arduino("/dev/ttyACM1")
# Change to your port
from time import sleep
class ProjectNameGUI(App):
    tester = ObjectProperty(DPEAButton)

    def build(self):
        """
        Build the application
        :return: Kivy Screen Manager instance
        """
        return SCREEN_MANAGER

class MainScreen(Screen):
    xcv = 0
    def switch(self):
        if self.xcv == 1:
            board.digital[13].write(0)
            self.xcv = 0
            print(self.xcv)
        elif self.xcv == 0:
            board.digital[13].write(1)
            self.xcv = 1
            print(self.xcv)


# print("Start blinking D13")
# print(board.digital[13])

# while True:
#     board.digital[13].write(1)
#     sleep(1)
#     board.digital[13].write(0)
#     sleep(1)

Builder.load_file('test.kv')
SCREEN_MANAGER.add_widget(MainScreen(name='main'))

if __name__ == '__main__':
    ProjectNameGUI().run()