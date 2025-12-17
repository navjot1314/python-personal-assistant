"""
Feature Module

Implements core assistant features such as information queries,
responses, and utility-based interactions.
"""
from logging import PlaceHolder
from urllib.parse import uses_relative
from geopy import location
import pywhatkit
import wikipedia
from pywikihow import search_wikihow
import os
import webbrowser as web
import pyttsx3
from time import sleep
import requests
from pytube import YouTube
import webbrowser
from datetime import datetime
from datetime import time
from playsound import playsound

# geopy==2.0.0
# geocoder==1.38.1

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
newVoiceRate = 100
engine.setProperty('rate' , newVoiceRate)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def GoogleSearch(term):
    query = term.replace("nebula","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")

    writeab = str(query)


   

    Query = str(term)

    pywhatkit.search(Query)

    

    if 'how to' in Query:

        max_result = 1

        how_to_func = search_wikihow(query=Query,max_results=max_result)

        assert len(how_to_func) == 1

        how_to_func[0].print()

        Speak(how_to_func[0].summary)

    else:

        search = wikipedia.summary(Query,2)

        Speak(f": According To Your Search : {search}")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You Sir .")


    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

    sleep(2)
    click(x=942,y=59)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):


        url = YouTube(link)


        video = url.streams.first()


        video.download('')#download location


    Download(Link)


    Speak("Done Sir , I Have Downloaded The Video .")

    Speak("You Can Go And Check It Out.")


    os.startfile('')#start file or start application location 

def SpeedTest():

    os.startfile("") #gui location 

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)

def My_Location():

    op = "https://www.google.com/maps/place/Delhi/@28.6472799,76.8130619,83757m/data=!3m2!1e3!4b1!4m5!3m4!1s0x390cfd5b347eb62d:0x37205b715389640!8m2!3d28.7040592!4d77.1024902"

    Speak("Checking....")

    web.open(op)

    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    Speak(f"Sir , You Are Now In {state , country} .")

def Download():
    Speak("Please paste the YouTube link in the terminal.")
    link = input("Paste YouTube link here: ")
    try:
        url = YouTube(link)
        video = url.streams.first()
        video.download('')#location 
        
        Speak("Done Sir, I have downloaded the video.")
        Speak("You can go and check it out.")
        
        os.startfile('')#location
    except Exception as e:
        Speak(f"Sorry, I couldn't download the video. An error occurred: {e}")

def My_Location():
    op = "https://www.google.com/maps/place/Delhi/@28.6472799,76.8130619,83757m/data=!3m2!1e3!4b1!4m5!3m4!1s0x390cfd5b347eb62d:0x37205b715389640!8m2!3d28.7040592!4d77.1024902"
    Speak("Checking....")
    web.open(op)
    
    try:
        ip_add = requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_q = requests.get(url)
        geo_d = geo_q.json()
        
        state = geo_d['city']
        country = geo_d['country']
        
        Speak(f"Sir, You Are Now In {state, country}.")
    except Exception as e:
        Speak(f"Sorry, I couldn't determine your location. An error occurred: {e}")

def GoogleSearch(term):
    query = term.replace("proton", "").replace("what is", "").replace("how to", "").replace("what do you mean by", "").strip()
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    Speak(f"Searching Google for {term}")

    if 'how to' in term.lower():
        max_result = 1
        how_to_func = search_wikihow(query=term, max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        Speak(how_to_func[0].summary)
    else:
        search_summary = wikipedia.summary(term, sentences=2)
        Speak(f"According to your search: {search_summary}")

def set_alarm(alarm_time):
    sound_file = ""  # Predefined sound file path
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Alarm! Wake up!")
            playsound(sound_file)
            break
        time.sleep(1)

