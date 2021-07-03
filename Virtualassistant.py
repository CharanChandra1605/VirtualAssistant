import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import webbrowser
import psutil
import os
import random


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():


    try:
        with sr.Microphone() as source:

            voice = listener.listen(source)
            command = listener.recognize_google(voice )
            command = command.lower()
            print(command)


    except sr.UnknownValueError:
        talk("Sir can you please repeat again")
        with sr.Microphone() as source:
            while True:
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()

                return command




    except sr.RequestError:
        talk("Error")
    return command




def run_alexa():
    command = take_command()

    if 'play' in command or 'song' in command or 'youtube' in command :
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)


    elif 'what' in command  or 'who' in command or 'when' in command :

        topic = command.replace('what','')
        talk(topic)
        info = wikipedia.summary(topic,2)
        print(info)
        talk(info)

    elif 'time' in command :
        time =datetime.datetime.now().strftime('%I:%M %p')
        talk(time)
        print(time)
    elif 'whatsapp' in command or 'chat' in command :
        talk('opening whatsapp')
        webbrowser.open("https://web.whatsapp.com/")
        
    elif 'mail' in command or 'gmail' in command:
        talk('opening mail')
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        
    elif'search' in command or 'open' in command:
        print(command)
        search = command.replace('search','')
        pywhatkit.search(search)
        #pywhatkit.close_tab()

    elif 'battery' in command:
        battery = psutil.sensors_battery()
        print("Battery percentage : " , battery.percent)
        talk(battery.percent)

    elif 'shutdown' in command or 'off' in command:
        shut_down = talk("Sir ,Do you want to shutdown the system")
        x = take_command()
        if(x == 'yes'):
            talk("shutdowning...")
            os.system("shutdown /s /t 1")
    elif 'bye' in command or 'nothing' in command or 'leave' in command:
       talk("bye sir ")




hour = datetime.datetime.now().hour
if hour>=0 and hour<12:
    talk("Hello sir ,Good Morning")
elif hour>=12 and hour<18:
    talk("hello Sir ,Good afternoon")
else:
    talk("Hello Sir ,  Good Evening")

talk("How can I  Help you ")

while True:
   run_alexa()




