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
from datetime import datetime
from time import sleep

# setting
from setting import menu_xlsx_path, command_data_dict

# order process modules
# process order
from process_order import load_xlsx, process_data_to_menu, process_price_with_order

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

        self.last_order = ''

    def line_speaker(self, texts,lang='zh-tw'):
        with NamedTemporaryFile(delete=True) as fp:
            tts = gTTS(text=texts,lang=lang)
            tts.save("{}.mp3".format(fp.name))
            if self.has_mixer:
                mixer.music.load('{}.mp3'.format(fp.name))
                mixer.music.play()
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
        data_dict = load_xlsx(file_name=menu_xlsx_path)
        menu_dict = process_data_to_menu(data_dict)
        self.line_speaker('您好，很高興為您服務，請問要做些甚麼？')
        order_line = self.listener()
            
        # 問好
        if '你好' in order_line:
            self.line_speaker('你好。')
            if self.master!=None:
                self.line_speaker('我的'+self.master)
        
        # 我的名字是
        elif '我的名字是' in order_line or '我是' in order_line:
            self.master=order_line.split('是')[-1]
            self.line_speaker('你就是我的Master嗎？'+self.master)

        # 有什麼吃的？
        elif '吃的' in order_line:
            eat_count = 0
            self.line_speaker('想吃飯還是麵？')
            while(eat_count<2):
                order_line = self.listener()
                if '飯' in order_line:
                    self.line_speaker('我們沒有飯')
                    eat_count+=1
                elif '麵' in order_line:
                    self.line_speaker('我們沒有麵')
                    eat_count+=1
                else:
                    self.line_speaker('我們沒有這個')
            self.line_speaker('我們有水餃')

        # 機率論
        elif '機率' in order_line:
            self.line_speaker('請描述你所要計算的機率問題。講完後請說我說完了')
            while(not '完' in order_line):
                order_line = self.listener()
            self.line_speaker('請問所求為會發生還是不會發生的機率？')
            order_line = self.listener()
            while(not '會' in order_line):
                order_line = self.listener()
            if '不會' in order_line:
                self.line_speaker('二分之一')
            else:
                self.line_speaker('二分之一')

        # 點餐
        elif '餐' in order_line:
            total_order = ''
            self.line_speaker('請問要點些什麼呢？')
            while(1):
                order_menu_line = self.listener()
                if '和' in order_menu_line or '個' in order_menu_line:
                    total_order+=order_menu_line+'和'
                elif '餐' in order_menu_line or '點完' in order_menu_line:
                    # 點完餐
                    break
                else:
                    self.line_speaker('不好意思，請再說一次。')
            self.line_speaker(process_price_with_order(menu_dict, total_order))

        # 問時間，幾點了
        elif ('時間' in order_line) or ('幾點' in order_line):
            now = datetime.now()
            res_text = '現在時間是 %d 點 %d 分 %d 秒' % (now.hour, now.minute, now.second)
            self.line_speaker(res_text)

        # 離開
        elif '離開' in order_line or '結束' in order_line:
            self.line_speaker('很高興為您服務，很期待您下次光顧。')
            sleep(6)
        
        # not any option upper
        else:
            self.line_speaker('不好意思，請再說一次。')
            
    def __call__(self):
        self.order_manage()

if __name__ == '__main__':
    order_bot = Order_Bot('text')
    order_bot.mode = 'voice2'
    order_bot()