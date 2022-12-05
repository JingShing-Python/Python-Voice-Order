import speech_recognition as sr
class Voice_Detect_Helper:
    def __init__(self, language='zh-TW', file_path="test.wav"):
        self.language = language
        # default is english
        self.file_path = file_path
        self.r = sr.Recognizer()
        self.result = None
    def detect_voice(self):
        with sr.WavFile(self.file_path) as source:
            # reduce ambient sound and noise
            # self.r.adjust_for_ambient_noise(source)
            # load wav
            audio = self.r.record(source)
        try:
            # using google service
            self.result = self.r.recognize_google(audio,language=self.language)
            print("Transcription: " + self.result)
        except:
            print("Could not understand audio")

    def __call__(self):
        self.detect_voice()