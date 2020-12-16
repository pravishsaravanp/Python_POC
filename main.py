# Date - 16-12-2020
# By - Pravish Saravan P
# Alexa/Siri replica

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer() 
engine = pyttsx3.init()
flag = True

# Voice from Python code
def speak(command):
    engine.say(command)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[7].id)
            # speak('I am Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jeff' in command:
                command = command.replace('%jeff', '')
                print(command)
            # elif 'jeff' not in command:
            #     print('Please call me as JEFF')
            #     speak('Please call me as JEFF')
    except:
        pass
    return command


def run_jeff():
    command = take_command()
    if 'name' in command:
        print('I\'m JEFF, your assist')
        speak('I\'m JEFF, your assist')
    elif 'play' in command:
        youtube = command.replace('play', '')
        print('Playing ' + youtube)
        speak(youtube)
        pywhatkit.playonyt(youtube)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S %p')
        print(time)
        speak(time)
    elif 'search' in command:
        search = command.replace('search ','')
        search_info = wikipedia.summary(search,2)
        print(search_info)
        speak(search_info)
    elif 'joke' in command:
        joke = pyjokes.get_joke('en')
        print(joke)
        speak(joke)
    elif 'thank you' or 'bye' in command:
        print('Nice talking to you!')
        speak('Nice talking to you!')
        flag = False
    elif 'fuck' or 'suck' in command:
        speak('Please be polite')
    else:
        print('Please say again!')
        speak('Please say again!')


while flag is True:
    run_jeff()
