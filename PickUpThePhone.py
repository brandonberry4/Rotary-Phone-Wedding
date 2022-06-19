import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN) #red wire
GPIO.setup(37, GPIO.OUT) #green led
GPIO.setup(35, GPIO.OUT) #red led


def bounce(channel):
    if GPIO.input(12):
        print ("Up")
        GPIO.output(37, GPIO.HIGH)
        GPIO.output(35, GPIO.LOW)
    else:
        print ("Down")
        GPIO.output(37, GPIO.LOW)
        GPIO.output(35, GPIO.HIGH)

GPIO.add_event_detect(12, GPIO.BOTH, callback = bounce)

try:
    print("Start")
    pass
except KeyboardInterrupt:
    GPIO.cleanup()