import RPi.GPIO as GPIO
from time import sleep
import time
import pyaudio
import wave

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN) #red wire
GPIO.setup(37, GPIO.OUT) #green led
GPIO.setup(35, GPIO.OUT) #red led

form_1 = pyaudio.paInt16
chans = 1
samp_rate = 16000
chunk = 4096
record_secs = 100
dev_index = 1
moment = time.strftime("%Y-%b-%d__%H_%M_%S", time.localtime())
wav_output_filename = open(moment + '.wav', 'wb')
audio = pyaudio.PyAudio()
frames = []

def bounce(channel):
    if GPIO.input(12):
        print ("Up")
        stream = audio.open(format = form_1, rate = samp_rate, channels = chans, input_device_index = dev_index, input = True, frames_per_buffer = chunk)
        GPIO.output(37, GPIO.HIGH)
        GPIO.output(35, GPIO.LOW)

        print("Recording")

        for ii in range(0, int((samp_rate/chunk)*record_secs)):
            data = stream.read(chunk)
            frames.append(data)

    else:
        print ("Down")
        GPIO.output(37, GPIO.LOW)
        GPIO.output(35, GPIO.HIGH)

GPIO.add_event_detect(12, GPIO.BOTH, callback = bounce)

try:
    bounce(12)
    if bounce(12) == ("Down"):
        print("Done recording")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        wavefile = wave.open(wav_output_filename, 'wb')
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()
except KeyboardInterrupt:
    GPIO.cleanup()
    quit()