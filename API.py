import os
import requests
from dotenv import load_dotenv


def get_weather_forecast(city, country_code, api_key):
    url = (
        "https://api.openweathermap.org/data/2.5/forecast"
        f"?q={city},{country_code}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


def print_forecast(data, city, country_code):
    print(f"Weather forecast for {city}, {country_code}:\n")

    for forecast in data["list"]:
        dt_txt = forecast["dt_txt"]
        temp = forecast["main"]["temp"]
        description = forecast["weather"][0]["description"]
        wind_speed = forecast["wind"]["speed"]

        print(f"Date & Time: {dt_txt}")
        print(f"Temperature: {temp}°C")
        print(f"Weather: {description}")
        print(f"Wind Speed: {wind_speed} m/s")
        print("-" * 40)


def main():
    load_dotenv()

    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    city = os.getenv("CITY")
    country_code = os.getenv("COUNTRY_CODE")

    if not all([api_key, city, country_code]):
        print("Missing environment variables. Please check your .env file.")
        return

    data = get_weather_forecast(city, country_code, api_key)

    if data and "list" in data:
        print_forecast(data, city, country_code)
    elif data:
        print(f"Error from API: {data.get('message', 'Unknown error')}")


if __name__ == "__main__":
    main()
