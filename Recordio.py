import pyaudio
import wave
import time

def Record():
        audio = pyaudio.PyAudio()

        for ii in range (audio.get_device_count()):
            print(audio.get_device_info_by_index(ii).get('name'))

        form_1 = pyaudio.paInt16
        chans = 1
        samp_rate = 16000
        chunk = 4096
        record_secs = 60
        dev_index = 1
        moment = time.strftime("%Y-%b-%d__%H_%M_%S", time.localtime())
        wav_output_filename = open(moment + '.wav', 'wb')

        stream = audio.open(format = form_1, rate = samp_rate, channels = chans, input_device_index = dev_index, input = True, frames_per_buffer = chunk)
        print("recording")
        frames = []

        for ii in range (0, int((samp_rate/chunk)*record_secs)):
            data = stream.read(chunk)
            frames.append(data)

        print("done recording")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        wavefile = wave.open(wav_output_filename, 'wb')
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()

if __name__ == '__main__':
    try:
        Record()
    except KeyboardInterrupt:
        quit()