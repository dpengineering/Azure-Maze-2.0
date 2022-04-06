from pyfirmata import Arduino, util
from time import sleep

board = Arduino("/dev/ttyACM1") # Change to your port
print("Start blinking D13")
# board.digital[13].write(1)
while True:
    board.digital[13].write(1)
    sleep(1)
    board.digital[13].write(0)
    sleep(1)



# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
