import requests
import json

def get_weather_data(location):
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    data = json.loads(response.text)
    return data

def display_weather(data):
    if data["cod"] != "404":
        name = data["name"]
        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        print(f"Weather for {name}:")
        print(f"Description: {desc}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("Location not found. Please try again.")

def main():
    location = input("Enter a city name or zip code: ")
    weather_data = get_weather_data(location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
