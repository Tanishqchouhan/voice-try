import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests as re
import json
import smtplib
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("how can i help you")       
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:

        print("Recognizing...")    
        
            
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
            
        print("Say that again please...")  
        return "None"
    return query


def cancelflight(flightname,date,source,destination,flight_class):
    x = {"name": flightname,"date": date,"source": source,"destination": destination,"class" :flight_class }
    cancel = json.dumps(x)
    print(cancel)
    
def bookflight(flightname,date,source,destination,flight_class):
    x = {
            "name": flightname,
            "date": date,
            "source": source,
            "destination": destination,
            "class" :flight_class 
        }


    book = json.dumps(x)


    print(book)



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")


        elif 'flight' in query:
            if 'book' in query:
                try:
                    speak ("which flight")
                    print ("which flight")
                    flightname = takeCommand()    
                    speak("which date?")
                    print ("which date?")
                    date = takeCommand()
               
                    speak("from where?")
                    print ("from where?")
                    source = takeCommand()
                    speak("to where")
                    print ("to where?")
                    destination = takeCommand()
                    speak("class ?")
                    print ("class?")
                    flight_class = takeCommand()   
                    bookflight(flightname,date,source,destination,flight_class)
                except Exception as e:
                    print(e)
                    speak("sorry")    

            if 'cancel' in query:
                try:
                    speak ("which flight")
                    print ("which flight")
                    flightname = takeCommand()    
                    speak("which date?")
                    print ("which date?")
                    date = takeCommand()
               
                    speak("from where?")
                    print ("from where?")
                    source = takeCommand()
                    speak("to where")
                    print ("to where?")
                    destination = takeCommand()
                    speak("class ?")
                    print ("class?")
                    flight_class = takeCommand()   
                    cancelflight(flightname,date,source,destination,flight_class)  


                except Exception as e:
                    print(e)
                    speak("sorry")


        
        
