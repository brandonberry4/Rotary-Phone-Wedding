import RPi.GPIO as GPIO
from time import sleep
import time
import pyaudio
import wave
import PickUpThePhone
import Recordio

try:
    PickUpThePhone.bounce(12)
    Recordio.Record()
except KeyboardInterrupt:
    quit()
