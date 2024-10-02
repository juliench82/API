import os
import requests
from dotenv import load_dotenv

# Environment variables
load_dotenv()

api_key = os.getenv("OPENWEATHERMAP_API_KEY")
city = os.getenv("CITY")
country_code = os.getenv("COUNTRY_CODE")

# OpenWeatherMap API URL
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country_code}&appid={api_key}&units=metric"

# Fetch weather data
response = requests.get(url)
data = response.json()

# Check if response contains 'list' key
if 'list' in data:
    # Extract and print the weather forecast
    forecasts = data['list']
    print(f"Weather forecast for {city}, {country_code}:\n")
    for forecast in forecasts:
        dt_txt = forecast['dt_txt']
        temp = forecast['main']['temp']
        weather_desc = forecast['weather'][0]['description']
        wind_speed = forecast['wind']['speed']
        print(f"Date & Time: {dt_txt}")
        print(f"Temperature: {temp}°C")
        print(f"Weather: {weather_desc}")
        print(f"Wind Speed: {wind_speed} m/s")
        print("-" * 40)
else:
    print("Error fetching weather data:", data.get("message", "Unknown error"))
