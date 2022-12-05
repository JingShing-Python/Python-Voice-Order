from recording_voice import Recording_Helper
from voice_detect import Voice_Detect_Helper

if __name__ == '__main__':
    recorder = Recording_Helper()
    voice_detecter = Voice_Detect_Helper()
    recorder()
    voice_detecter()