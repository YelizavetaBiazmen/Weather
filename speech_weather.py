import time
from gtts import gTTS
import os
import pygame
pygame.init()
import requests
import socket
def get_external_ip():      
    response = requests.get("https://api64.ipify.org?format=json")
    if response.status_code == 200:
        data = response.json()
        return data.get("ip") 

def get_location(ip_address):     
    url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        city = data.get("city", "Unknown")
        #country = data.get("country", "Unknown")
        return city
    
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]    
        return city_name+ " "+ weather_description+" "+str(temperature)+"degrees "+str(humidity) + "%"

def say(txt):
    lg = "en" 
    tts = gTTS(text = txt, lang=lg)
    tts.save("./speech.mp3")
    pygame.mixer.music.load("./speech.mp3")
    pygame.mixer.music.play()


external_ip = get_external_ip()
location = get_location(external_ip)
   #print("Location:", location)
api_key = "306af8746611a374228c97a864aa3e18"
city_name = location
#input("Введите название города: ")
weather_info = get_weather(city_name, api_key)
print(weather_info)
say(weather_info)   
                    
time.sleep(3)
