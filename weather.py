# -*- coding: utf-8 -*-
#!/usr/bin/python3
'''
Find the current temperature using your zip code and the OpenWeatherMap API
http://openweathermap.org/
Uses imperial units

By Max Thauer
'''

import urllib.request, urllib.error, urllib.parse
from urllib.request import urlopen
import json, time

key = "YOUR_KEY_HERE"

zipcode = input("What is your zip code?: ")
zipcode = str(zipcode)
url = str("http://api.openweathermap.org/data/2.5/weather?zip=" + zipcode + ",us&units=imperial&APPID=" + key + "")

result = urllib.request.urlopen(url)
content = result.read()
data = json.loads(content.decode('utf8'))

latitude = data['coord']['lat']
longitude = data['coord']['lon']

description = data['weather'][0]['description']
temperature = data['main']['temp']
high = data['main']['temp_max']
low = data['main']['temp_min']
humidity = data['main']['humidity']
pressure = data['main']['pressure']
speed = data['wind']['speed']
deg = data['wind']['deg']
sunrise = data['sys']['sunrise']
sunup = time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(sunrise))
sunset = data['sys']['sunset']
sundown = time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(sunset))


print ("")
print(("City: " + data['name']))
print(("Latitude: ") + repr(latitude) + ("˚ ") + ("Longitude: ") + repr(longitude) + ("˚"))
print(("Description: ") + (description))
print ("")

print(("Current Temperature: ") + repr(temperature) + ("˚"))
print(("High: ") + repr(high) + ("˚ ") + ("Low: ") + repr(low) + ("˚"))
print(("Humidity: ") + repr(humidity) + ("%"))
print(("Pressure: ") + repr(pressure) + (" hpa"))
print(("Wind Speed: ") + repr(speed) + (" MPH") + ("  Direction: ") + repr(deg))
print ("")
print ("Sunrise: " + (sunup) + " UTC")
print ("Sunset:  " +(sundown) + " UTC")
print ("")
