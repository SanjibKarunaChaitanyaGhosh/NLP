import speech_recognition as sr
# text to speech = PyTTSX3
# speech to text = SpeechRecognition


# sr.Recognizer() = brain
# Microphone() = ears
# .listen() = waiting for your loud words
# .recognize_google() = sends audio to Gooogle's free speech API for text


# initalize recognizer
r = sr.Recognizer()

# Use Microphone as source
#print(sr.Microphone())

with sr.Microphone() as source:
    print("🎤 Speak Now")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You Said: ", text)

except sr.UnknownValueError:
    print("Bruh, I couldn't understand what you are said.")

except sr.RequestError:
    print("Internet issue, Google ain't listening right now.")
