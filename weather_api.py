# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 14:40:29 2022

@author: shanthu3769
"""


#07eecd19c8c0933bfc0ce46954ea9a02

#importing modules
import os
import requests
from datetime import datetime
import time

#description of projectk
print("Hello")
time.sleep(0.5)
print("Here, you can find weather in your city!")
time.sleep(1)
#access API key
#weather_key = os.environ["weather"]
#location from user
location = input("Enter location: ")
#URL
api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=07eecd19c8c0933bfc0ce46954ea9a02"
#HTTP request
r=requests.get(api_link)
#convert the data in 'r' into dictionary
data=r.json()
if(data["cod"]=="404"):
        print(f"Invalid city: {location}\nEnter valid city")
        exit()
else:
    temp= data["main"]["temp"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    speed = data["wind"]["speed"]
    descr = data["weather"][0]["description"]
    date_time = datetime.now().strftime("%D %M %Y | %H:%M:%S %p")
print("||----------------------------------------------------------------||")
print(f"  Location: {location} ||||  Date&Time : {date_time}")
time.sleep(1)
print(f"  Scenerio : {descr}")
time.sleep(1)
print(f"  Temperature : {temp}")
time.sleep(1)
print(f"  Pressure : {pressure}")
time.sleep(1)
print(f"  Speed : {speed}")
time.sleep(1)
print("||----------------------------------------------------------------||")
time.sleep(1)
print("Thank You!!")
