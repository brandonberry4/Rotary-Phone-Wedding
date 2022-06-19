import pyaudio
audio = pyaudio.PyAudio()
form_1 = pyaudio.paInt16
chans = 1
samp_rate = 16000
chunk = 4096
record_secs = 100
dev_index = 1

stream = audio.open(format = form_1, rate = samp_rate, channels = chans, input_device_index = dev_index, input = True, frames_per_buffer = chunk)

try:
    while True:
        data = stream.recv(chunk)
        stream.write(data)
except KeyboardInterrupt:
    pass
