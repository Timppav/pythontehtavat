import requests
import json

search = input("Anna paikkakunnan nimi: ")

api_key = ""
units = "metric"
geocode = "http://api.openweathermap.org/geo/1.0/direct?q=" + search + "&limit=5&appid=" + api_key

try:
    response = requests.get(geocode)
    if response.status_code == 200:
        json_response = response.json()
        for n in json_response:
            lat = n["lat"]
            lon = n["lon"]
            weather = ("https://api.openweathermap.org/data/2.5/weather?"
                       "lat=" + str(lat) + "&lon=" + str(lon) + "&units=" + units + "&appid=" + api_key)
            json_weather = requests.get(weather).json()
            name = json_weather["name"]
            country = json_weather["sys"]["country"]
            temperature = json_weather["main"]["temp"]
            feels_like = json_weather["main"]["feels_like"]
            rain = json_weather["weather"][0]["description"]
            print(f"\nPaikkakunta: {name}\nMaa: {country}\nLämpötila: {temperature}°C\n"
                  f"Tuntuu kuin: {feels_like}°C\nSäätila: {rain}")
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
