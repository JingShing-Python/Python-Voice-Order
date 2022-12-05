import pyaudio
import wave

class Recording_Helper:
    def __init__(self, chunk = 1024, sample_format = pyaudio.paInt16, channels = 2, fs = 44100, seconds = 5, file_name = "test.wav"):
        # sample chunk size
        self.chunk = chunk
        # sample format: paFloat32, paInt32, paInt24, paInt16, paInt8, paUInt8, paCustomFormat
        self.sample_format = sample_format
        # sound channel
        self.channels = channels
        # sample frequency rate: 44100 ( CD ), 48000 ( DVD ), 22050, 24000, 12000 and 11025
        self.fs = fs
        # recording seconds
        self.seconds = seconds
        # recording file name
        self.file_name = file_name

        self.p = pyaudio.PyAudio()
        # init pyaudio object

    def recording_voice(self):
        print("starting recording...")

        # active voice stream
        stream = self.p.open(format=self.sample_format, channels=self.channels, rate=self.fs, frames_per_buffer=self.chunk, input=True)

        frames = []
        # voice list

        for i in range(0, int(self.fs / self.chunk * self.seconds)):
            # record voice into list
            data = stream.read(self.chunk)
            frames.append(data)

        # stop recording
        stream.stop_stream()
        # close stream
        stream.close()
        self.p.terminate()

        print('stop recording...')

        # open voice file
        wf = wave.open(self.file_name, 'wb')
        # set channel
        wf.setnchannels(self.channels)
        # set format
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        # set sampling frequency rate
        wf.setframerate(self.fs)
        # save
        wf.writeframes(b''.join(frames))
        wf.close()

    def __call__(self):
        self.recording_voice()
