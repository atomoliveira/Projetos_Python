#Escreva um programa que seja como o Alexa da Google 

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("==========================================")
        print("                 SEDNA                    ")
        print("==========================================")
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            command = ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            command = ""
    return command.lower()

def process_command(command):
    if 'time' in command:
        now = datetime.datetime.now()
        speak(f"The current time is {now.strftime('%H:%M:%S')}")
    elif 'date' in command:
        today = datetime.datetime.now()
        speak(f"Today's date is {today.strftime('%Y-%m-%d')}")
    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open('http://www.google.com')
    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open('http://www.youtube.com')
    elif 'stop' in command:
        speak("Goodbye!")
        return False
    else:
        speak("I did not understand that command.")
    return True

def main():
    speak("Hi, May I help you?")
    running = True
    while running:
        command = listen()
        if command:
            running = process_command(command)

if __name__ == "__main__":
    main()
