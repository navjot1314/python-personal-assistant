"""
NASA API Module

Fetches and processes data from NASA public APIs
to provide space-related information via the assistant.
"""

import requests
import cartopy.crs as ccrs 
import matplotlib.pyplot as plt
import os
from PIL import Image
import random
import pyttsx3
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

Api_Key = ""#take the api key and add here 

def NasaNews(Date):

    Speak("Extracting Data From Nasa . ")

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)

    Params = {'date':str(Date)}
    
    r = requests.get(Url,params = Params)

    Data = r.json()

    Info = Data['explanation']

    Title = Data['title']

    Image_Url = Data['url']

    Image_r = requests.get(Image_Url)

    FileName = str(Date) + '.jpg'

    with open(FileName,'wb') as f:

        f.write(Image_r.content)

    Path_1 = "" + str(FileName)

    Path_2 = "" + str(FileName)

    os.rename(Path_1, Path_2)

    img = Image.open(Path_2)

    img.show()

    Speak(f"Title : {Title}")
    Speak(f"According To Nasa : {Info}")

def Summary(Boby):

    list__ = ('2','3','4','5')

    value = random.choice(list__)

    path = " " + str(value) + ".jpg"#add the location where the pictures should be added 

    os.startfile(path)

    name = str(Boby)

    url = "https://hubblesite.org/api/v3/glossary/" + str(name)

    r = requests.get(url)

    Data = r.json()

    if len(Data) != 0:

        retur =  Data['definition']

        Speak(f"According To The Nasa : {retur}")

    else:

        Speak("No Data Available , Try Again Later!")

def MarsImage():
    name = 'curiosity'
    date = '2020-12-3'
    api_key = ''  # Replace with your actual API key

    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={api_key}"
    r = requests.get(url)
    data = r.json()

    photos = data['photos'][:20]

    try:
        for index, photo in enumerate(photos):
            camera = photo['camera']
            rover = photo['rover']
            rover_name = rover['name']
            camera_name = camera['name']
            full_camera_name = camera['full_name']
            date_of_photo = photo['earth_date']
            img_url = photo['img_src']

            p = requests.get(img_url)
            img = f'{index}.jpg'
            img_path = os.path.join("", img)#location of you path 

            with open(img_path, 'wb') as file:
                file.write(p.content)

            os.startfile(img_path)

            Speak(f"This Image Was Captured With: {full_camera_name}")
            Speak(f"This Image Was Captured On: {date_of_photo}")

    except Exception as e:
        Speak(f"There is An Error: {e}")

def IssTracker():
    url = "http://api.open-notify.org/iss-now.json"
    r = requests.get(url)
    Data = r.json()
    dt = Data['timestamp']
    lat = Data['iss_position']['latitude']
    lon = Data['iss_position']['longitude']
    
    Speak(f"Time And Date : {dt}")
    Speak(f"Latitude : {lat}")
    Speak(f"Longitude : {lon}")
    
    plt.figure(figsize=(10, 8))
    ax = plt.axes(projection = ccrs.PlateCarree())
    ax.stock_img()
    
    plt.scatter(float(lon), float(lat), color = 'blue', marker= 'o')
    plt.show()

def Astro(start_date, end_date):
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"
    r = requests.get(url)
    Data = r.json()
    Total_Astro = Data['element_count']
    neo = Data['near_earth_objects']
    
    Speak(f"Total Asteroids Between {start_date} and {end_date} Is: {Total_Astro}")
    Speak("Exact Data For Those Asteroids Are Listed Below.")
    
    for body in neo[start_date]:
        id = body['id']
        name = body['name']
        absolute = body['absolute_magnitude_h']
        print(id, name, absolute)


