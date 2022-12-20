# voice process modules
# detect voice
from speech_recognition import Recognizer, Microphone, WavFile
from pyaudio import PyAudio, paInt16
import wave
# generate voice
from pygame import mixer
from tempfile import NamedTemporaryFile
from gtts import gTTS

# time
from time import sleep

# setting
from setting import command_data_dict, module_data_dict

class Order_Bot:
    def __init__(self, mode = 'voice1'):
        # speaker init
        self.has_mixer = False
        try:
            mixer.init()
            self.has_mixer = True
        except:
            pass
        # mode: voice1, voice2, text
        self.mode = mode
        # recognizer init    
        self.recognizer = Recognizer()
        # user name
        self.master = None
        self.modules = module_data_dict

        self.last_order = ''

    def line_speaker(self, texts,lang='zh-tw'):
        with NamedTemporaryFile(delete=True) as fp:
            tts = gTTS(text=texts,lang=lang)
            tts.save("{}.mp3".format(fp.name))
            if self.has_mixer:
                mixer.music.load('{}.mp3'.format(fp.name))
                mixer.music.play()
        command_data_dict['bot_reply']=texts
        print(texts)

    def listener(self):
        if self.mode == 'text':
            result = input()
        elif self.mode == 'tk_text':
            while(not command_data_dict['is_command']):
                pass
            command_data_dict['is_command'] = False
            result = command_data_dict['command_line']
            print(result)
        elif self.mode == 'voice1':
            # this mode using google to record
            # so it takes long time
            result = None
            while(result == None):
                with Microphone() as source:
                    # recognizer.adjust_for_ambient_noise(source)
                    audio = self.recognizer.listen(source)
                try:
                    result = self.recognizer.recognize_google(audio,language = 'zh-tw')
                except:
                    continue
            print(result)
        elif self.mode == 'voice2':
            result = None
            while(result == None):
                # sample chunk size
                chunk = 1024
                # sample format: paFloat32, paInt32, paInt24, paInt16, paInt8, paUInt8, paCustomFormat
                sample_format = paInt16
                # sound channel
                channels = 2
                # sample frequency rate: 44100 ( CD ), 48000 ( DVD ), 22050, 24000, 12000 and 11025
                fs = 44100
                # recording seconds
                seconds = 5
                # init pyaudio object
                p = PyAudio()

                print("starting recording...")

                # active voice stream
                stream = p.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True)
                frames = []
                # voice list
                for _ in range(0, int(fs / chunk * seconds)):
                    # record voice into list
                    data = stream.read(chunk)
                    frames.append(data)
                # stop recording
                stream.stop_stream()
                # close stream
                stream.close()
                p.terminate()
                print('stop recording...')
                
                with NamedTemporaryFile(delete=True) as fp:
                    # open voice file
                    wf = wave.open("{}.wav".format(fp.name), 'wb')
                    # set channel
                    wf.setnchannels(channels)
                    # set format
                    wf.setsampwidth(p.get_sample_size(sample_format))
                    # set sampling frequency rate
                    wf.setframerate(fs)
                    # save
                    wf.writeframes(b''.join(frames))
                    wf.close()
                    
                    with WavFile('{}.wav'.format(fp.name)) as source:
                        audio = self.recognizer.listen(source)
                        try:
                            result = self.recognizer.recognize_google(audio,language = 'zh-tw')
                        except:
                            continue
            print(result)
        self.last_order = result
        return result

    def order_manage(self):
        self.line_speaker('您好，很高興為您服務，請問要做些甚麼？')
        while(1):
            order_line = self.listener()

            key_token = None
            for key in self.modules.keys():
                if key in order_line:
                    key_token = key
                    break

            if not key_token == None:
                self.modules[key_token](self)
            # not any option upper
            else:
                self.line_speaker('不好意思，請再說一次。')
            
    def __call__(self):
        self.order_manage()

if __name__ == '__main__':
    order_bot = Order_Bot('text')
    # order_bot.mode = 'voice2'
    order_bot()