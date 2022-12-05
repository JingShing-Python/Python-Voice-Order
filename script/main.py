from voice_detect import Voice_Detect_Helper

def using_audio_to_talk(file_name = 'test.wav'):
    from recording_voice import Recording_Helper
    recorder = Recording_Helper(file_name=file_name)
    voice_detecter = Voice_Detect_Helper(file_path=file_name)
    recorder.recording_voice()
    voice_detecter.detect_voice()
    # you can get result from voice_detecter.result

def using_detecter_to_talk(file_name = 'test.wav'):
    voice_detecter = Voice_Detect_Helper(file_path=file_name)
    voice_detecter.listener()

if __name__ == '__main__':
    # method 1 using pyaudio to record
    # using_audio_to_talk()

    # method 2 using speech_recognition to record
    using_detecter_to_talk()