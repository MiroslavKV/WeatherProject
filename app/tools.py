import json
import requests

def get_weather(city = "Kyiv") -> dict | int:
    API_key = "9afe51f612758b792526d434e0acfb40"
    url = "https://api.openweathermap.org/data/2.5/weather"

    responce = requests.get(url, params={
        "q": city,
        "appid": API_key,
        "units": "metric",
        "lang": "ua"
        })

    if responce.status_code == 200:
        print(responce.url)
        return responce.json()
    else:
        return responce.status_code

    