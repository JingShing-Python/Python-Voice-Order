# process order
from process_order import load_xlsx, process_data_to_menu, process_price_with_order
# detect voice
import speech_recognition
# generate voice
from pygame import mixer
import tempfile
from gtts import gTTS

mixer.init()
def line_speaker(texts,lang='zh-tw'):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=texts,lang=lang)
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()
    print(texts)

r = speech_recognition.Recognizer()
def listener():
    result = None
    while(result == None):
        with speech_recognition.Microphone() as source:
            audio = r.listen(source)
        try:
            result = r.recognize_google(audio,language = 'zh-tw')
        except:
            continue
    print(result)
    return result

def order_manage():
    data_dict = load_xlsx()
    menu_dict = process_data_to_menu(data_dict)
    while(1):
        order_line = listener()
        if '餐' in order_line:
            # 點餐
            total_order = ''
            line_speaker('請問要點些什麼呢？')
            while(1):
                order_menu_line = listener()
                if '和' in order_menu_line or '個' in order_menu_line:
                    total_order+=order_menu_line+'和'
                elif '餐' in order_menu_line:
                    # 點完餐
                    break
            line_speaker(process_price_with_order(menu_dict, total_order))

        elif '離開' in order_line:
            break
        
if __name__ == '__main__':
    order_manage()