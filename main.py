import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import pyaudio
from twilio.rest import Client
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe'
#webbrowser.get(chrome_path).open("youtube.com")
#webbrowser.get(chrome_path).open("google.com")

#browser = webdriver.Chrome()
#browser.get("https://www.youtube.com")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("Jarvis 1 point o")
    speak("I am your Assistant")
    speak(assname)


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")


def takeCommand():
    r = sr.Recognizer()
    r.energy_threshold = 150
    r.adapt_threshold = True
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


database={

    "samuel hayden":"Head of uac mars facility"
}
if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    #username()

    while True:

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak("Here you go to Youtube\n")
            browser = webdriver.Chrome()
            browser.get("https://www.youtube.com")
            #webbrowser.open("youtube.com")
            #webbrowser.get(chrome_path).open("youtube.com")
            #webbrowser.get('chrome %s').open_new_tab("youtube.com")


        elif 'open google' in query:
            speak("Here you go to Google\n")
            browser = webdriver.Chrome()
            browser.get("https://www.google.com")
            #webbrowser.open("google.com")
            #webbrowser.get('chrome').open_new_tab("google.com")



        elif 'open source' in query:
            speak("writing the source of the code into the console")
            print("https://www.geeksforgeeks.org/voice-assistant-using-python/")
        elif 'search in the database for' in query:
            #query = query.replace("search in the database for", "")
            key = query.split("search in the database for ")[1]
            if key in database:
                speak(database[key])
            else:
                speak("the database not contain this entry")