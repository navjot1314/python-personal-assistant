"""
Utility Functions

Provides helper functions and shared logic
used across multiple assistant modules.
"""
from urllib.request import urlopen 
import psutil
import pyautogui
from playsound import playsound
import pyjokes
import speedtest
import pyttsx3
import requests


engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id) 
newVoiceRate = 144
engine.setProperty('rate' , newVoiceRate)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def internn():
    st = speedtest.Speedtest()
    dl = st.download()
    up = st.upload()
    print(f'sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed')
    speak(f'sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed')

def jokes():
	my_joke = pyjokes.get_joke('en', category='neutral')
	
	speak(my_joke)
	print(my_joke)

def screenshot():
	img = pyautogui.screenshot()
	img.save('')#add location to where the screensjhot should be added 
	playsound('')#add the location of the sound or audio

def news():
	main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey='#enter the api key 

	main_page = requests.get(main_url).json()
	articles = main_page['articles']
	head = []
	day=['first','second','third','fourth','fifth','sixth']
	for ar in articles:
		head.append(ar['title'])
	for i in range (len(day)):
		print(f"today's {day[i]} news is: {head[i]}")
		speak(f"today's {day[i]} news is: {head[i]}")

def cpu():
	cpu = str(psutil.cpu_percent())
	print(cpu)
	speak(f'you have used {cpu} of cpu.')
	battery = psutil.sensors_battery().percent
	print(battery)
	speak(f'you have used{battery} percent of battery.')

