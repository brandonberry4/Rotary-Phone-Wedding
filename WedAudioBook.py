import RPi.GPIO as GPIO
import math, sys, os
import subprocess
import socket
from time import sleep
import PickUpThePhone
import Recordio

try:
    #PickUpThePhone.bounce(12)
    while PickUpThePhone.bounce(12) == ('Up'):
        Recordio.Record()
except KeyboardInterrupt:
    GPIO.cleanup()
    quit()















# print("Setup")
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(40, GPIO.IN) #green wire
# GPIO.setup(38, GPIO.IN) #blue wire
# print("Setup done")

# c = 0
# last = 1

def count (pin):
    global c
    c = c + 1

# def count(channel):
#     global c
#     c = c + 1
#     if GPIO.input(40):
#         current = GPIO.input(40)
#         if (last != current):
#                  if (current == 0):
#                      GPIO.add_event_detect(38, GPIO.BOTH, bouncetime = 7)
#     else:
#         GPIO.remove_event_detect(38)
#         print("c")

#         number = int((c-1)/2)
#         print("You dialed", number)

#         c = 0

#         last = GPIO.input(40)

# GPIO.add_event_detect(40, GPIO.BOTH, callback = count)

while True:
    try:
        if GPIO.event_detected(40):
            current = GPIO.input(40)
            if (last != current):
                if (current == 0):
                    GPIO.add_event_detect(38, GPIO.BOTH, callback = count, bouncetime = 7)
                else:
                    GPIO.remove_event_detect(38)
                    print("c")

                    number = int((c-1)/2)
                    print("You dialed", number)

                    c = 0

                last = GPIO.input(40)

    except KeyboardInterrupt:
        GPIO.cleanup

# try:
#     print ("Try dialing numbers")
#     sleep(30)
#     print("Over")
# finally:
#     GPIO.cleanup()