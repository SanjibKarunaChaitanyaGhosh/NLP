import speech_recognition
import pyttsx3

def speak_now(command):
    voice= pyttsx3.init()
    voice.say(command)
    voice.runAndWait()

sr = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source2:
    print("Silence PLease")

    sr.adjust_for_ambient_noise(source2, duration = 2)
    print("Speak Now Please")

    audio2 = sr.listen(source2)

    textt=sr.recognize_google(audio2)

    textt=textt.lower()
    print("Did you say : - " +textt)

    speak_now(textt)