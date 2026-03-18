import sys
from time import time
from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyautogui
import random
from pywikihow import search_wikihow
from GoogleNews import GoogleNews as googlenews
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print (audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak ("Good Morning Sir!")

    elif hour >= 12 and hour <18:
        speak ("Good Afternoon Sir!")

    else:
        speak ("Good Evening Sir!")

    speak ("I am Jarvis. How may i help you") 

def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print ("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("Please Say That Again....")
        return "none"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening YouTube....")
            webbrowser.open("youtube.com")

        elif 'open notepad' in query:
            speak("Opening notepad....")
            notepadpath = "Copy The Notepad.exe path from your computer and paste it here "     # Example: notepadpath = "C:\\Windows\\notepad.exe"
            os.startfile(notepadpath)

        elif 'open google' in query:
            speak("What should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stack overflow' in query:
            speak("Opening Stackoverflow....")
            webbrowser.open("stackoverflow.com")

        elif 'open cgtrader' in query:
            speak("Opening CGtrader....")
            webbrowser.open("cgtrader.com")

        elif 'open turbosquid' in query:
            speak("Opening TurboSquid....")
            webbrowser.open("turbosquid.com")

        elif 'movies' in query:
            speak("Finding Some Movies For You....")
            webbrowser.open("https://www.rottentomatoes.com/browse/movies_in_theaters/")

        elif 'play music' in query:
            speak("Playing Music....")
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            a = random.choice(songs)
            os.startfile(os.path.join(music_dir, a))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")

        elif 'open code' in query:
            speak("Opening Visual Studio Code....")
            codepath = "Copy The Code.exe path from your computer and paste it here"   # Example: codepath = "D:\\Visual Studio Code\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'open discord' in query:
            speak("Opening Discord....")
            discordpath = "Copy The Discord.exe path from your computer and it here" # Example: discordpath = "C:\\Users\\ghosh\\AppData\\Local\\Discord\\Discord.exe"
            os.startfile(discordpath)
            
        elif 'open command prompt' in query:
            speak("Opening Command....")
            os.system("start cmd")

        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")


        elif "news" in query:
            from NewsRead import latestnews
            latestnews()    

        elif 'open whatsapp' in query:
            speak("Opening whatsapp....")
            webbrowser.open("web.whatsapp.com")

        elif "quit" in query:
            speak("All Servers. Closed....")
            sys.exit()

            
        elif "turn off" in query:
            speak("All Servers. Closed....")
            sys.exit()

        elif "activate how to do" in query:
            speak("How to do mod has been activated")
            while True:
                speak("please tell me what do you want to know")
                how = takecommand()
                try:
                    if 'exit' in how or 'close' in how:
                        speak ("Serching mod is closed")
                        break
                    else:
                        max_resuts = 1
                        how_to = search_wikihow(how, max_resuts)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this")

                

        if 'headlines' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.result()
            a=googlenews.gettext()
            print(a)
            speak(a)

        if 'tech' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('Tech')
            googlenews.result()
            a=googlenews.gettext()
            print(*a[1:5],sep=',')
            speak(*a[1:5],sep=',')

        if 'politics' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('Politics')
            googlenews.result()
            a=googlenews.gettext()
            print(*a[1:5],sep=',')
            speak(*a[1:5],sep=',')

        if 'sports' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('Sports')
            googlenews.result()
            a=googlenews.gettext()
            print(*a[1:5],sep=',')
            speak(*a[1:5],sep=',')

        if 'cricket' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('cricket')
            googlenews.result()
            a=googlenews.gettext()
            print(*a[1:5],sep=',')
            speak(*a[1:5],sep=',')
