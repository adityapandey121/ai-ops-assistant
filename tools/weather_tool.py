import os
import requests


class WeatherTool:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str):
        api_key = os.getenv("WEATHER_API_KEY")

        if not api_key:
            raise ValueError("WEATHER_API_KEY not set")

        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(self.BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        return {
            "city": city,
            "temperature_c": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }
