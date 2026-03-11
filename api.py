import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=25.03&longitude=121.56&current_weather=true"

response = requests.get(url)

data = response.json()

with open("weather.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data saved to weather.json")