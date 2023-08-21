import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
from bardapi import Bard
import os
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    now=int(datetime.datetime.now().hour)
    if now>=0 and now<12:
        speak("Good Morning user!")
    elif now>=12 and now<18:
        speak("Good Afternoon user!")
    else:
        speak("Good Evening user!")
    speak("i am Washeekaran your personel assistant how may i help you today")

def input():
    #It takes microphone input from the user
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said:{query}\n")   
    
    except Exception as e:
        #print(e)

        print("Say that again please......")
        return "None"
    return query


if __name__=="__main__":
    wishMe()

    while True:
        query = input().lower()
        #logic for executing tasks based on query
        if 'Wikipedia' in query:
            speak("Searching Wikipedia....")
            query=query.replace("Wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("www.google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")
        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strTime("%H:%M:%S")
            speak(f"Sir, the time is {strTime} ")
        elif 'open spiderman' in query:
            os.startfile("C:\Program Files (x86)\DODI-Repacks\Marvels SpiderMan Miles Morales")
        elif 'quit' in query:
            exit()


