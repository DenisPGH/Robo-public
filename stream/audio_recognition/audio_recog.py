# speechrecognition lib and pyttsx3 lib  or pyaudio
import speech_recognition
#  pip install pyaudio
import os

import pyttsx3
#audio=pyttsx3.init()
rec= speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic,duration=0.2)
            audio=rec.listen(mic)

            text=rec.recognize_google(audio)
            #text= text.lower()
            print(f"REC:{text}")
    except:
        pass
    # except speech_recognition.UnknownValueError():
    #     rec=speech_recognition.Recognizer()
    #     continue


