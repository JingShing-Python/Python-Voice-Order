# process order
from process_order import load_xlsx, process_data_to_menu, process_price_with_order
# detect voice
import speech_recognition
# generate voice
from pygame import mixer
import tempfile
from gtts import gTTS

# time
from datetime import datetime
from time import sleep

# speaker init
mixer.init()

def line_speaker(texts,lang='zh-tw'):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=texts,lang=lang)
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()
    print(texts)

# listener init()
recognizer = speech_recognition.Recognizer()
def listener():
    result = None
    while(result == None):
        with speech_recognition.Microphone() as source:
            # recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            result = recognizer.recognize_google(audio,language = 'zh-tw')
        except:
            continue
    print(result)
    return result

def order_manage():
    data_dict = load_xlsx()
    menu_dict = process_data_to_menu(data_dict)
    line_speaker('您好，很高興為您服務，請問要做些甚麼？')
    while(1):
        order_line = listener()
        # 點餐
        if '餐' in order_line:
            total_order = ''
            line_speaker('請問要點些什麼呢？')
            while(1):
                order_menu_line = listener()
                if '和' in order_menu_line or '個' in order_menu_line:
                    total_order+=order_menu_line+'和'
                elif '餐' in order_menu_line or '點完' in order_menu_line:
                    # 點完餐
                    break
                else:
                    line_speaker('不好意思，請再說一次。')
            line_speaker(process_price_with_order(menu_dict, total_order))

        # 問時間，幾點了
        elif ('時間' in order_line) or ('幾點' in order_line):
            now = datetime.now()
            res_text = '現在時間是 %d 點 %d 分 %d 秒' % (now.hour, now.minute, now.second)
            line_speaker(res_text)

        # 離開
        elif '離開' in order_line or '結束' in order_line:
            line_speaker('很高興為您服務，很期待您下次光顧。')
            sleep(6)
            break

        else:
            line_speaker('不好意思，請再說一次。')
        
if __name__ == '__main__':
    order_manage()