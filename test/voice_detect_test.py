import speech_recognition as sr
language = 'zh-TW'
# default is english
r = sr.Recognizer()
with sr.WavFile("test.wav") as source:
    # load wav
    audio = r.record(source)
try:
    # using google service
    print("Transcription: " + r.recognize_google(audio,language=language))
except:
    print("Could not understand audio")