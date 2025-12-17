"""
Python Personal Assistant – Main Controller

Acts as the entry point for the assistant.
Handles user interaction and routes commands
to feature and automation modules.
"""


import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 
newVoiceRate = 100
engine.setProperty('rate' , newVoiceRate)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
	
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.pause_threshold = 1
		audio = r.listen(source)
		said = ""
		
		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("Exception: " + str(e))
			
		return said.lower()


WAKE = "hello" 

while True:
	print("Listening.............")
	text = get_audio()
	
	if text and WAKE in text.lower():
		speak("hello")
		
		text = get_audio()
		
		from function import cpu
		cpu_status = ['status'] 
		for phrase in cpu_status:
			if phrase in text:
				cpu()
        
		from function import news
		news_info = ["news"]
		for phrase in news_info:
			if phrase in text:
				news()
		
		from function import jokes
		jokes_python = ["joke","jokes"]
		for phrase in jokes_python:
			if phrase in text:
				jokes()


		from Nasa import NasaNews
		nasanew = ["space news"]
		for phrase in nasanew:
			if phrase in text:
				NasaNews()

		from Nasa import IssTracker 
		

		from Features import GoogleSearch
		search_phrases = ["google", "search", "find"]
		if any(phrase in text.lower() for phrase in search_phrases):
			GoogleSearch(text)
			continue


		from Nasa import MarsImage
		mars_phrases = ["mars image", "mars photo", "curiosity","image","images"]
		if any(phrase in text.lower() for phrase in mars_phrases):
			MarsImage()
			continue

		iss_phrases = ["iss", "international space station", "space station"]
		if any(phrase in text.lower() for phrase in iss_phrases):
			IssTracker()
			continue



		
