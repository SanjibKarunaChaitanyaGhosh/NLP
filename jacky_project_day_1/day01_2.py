import speech_recognition
import pyttsx3
import webbrowser

if __name__ == "__main__":
    path= "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path))
    
    sr= speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        sr.adjust_for_ambient_noise(source)

        print("Please say somthing to open....")
        
        audio= sr.listen(source)

        print("Hearing....")
        
        try:
            destination = sr.recognize_google(audio)

            print("you asked to open : "+destination)

            webbrowser.get(path).open(destination)

        except Exception as e:
            print('error : '+str(e))