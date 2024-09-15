import requests
import sys
import datetime

# Replace with your OpenWeatherMap API key
API_KEY = 'c3aa4c5cf97c4794d42bad82962eba9b'

def get_weather_data(city_or_zip, forecast_type='current'):
    if forecast_type == 'current':
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': city_or_zip,
            'appid': API_KEY,
            'units': 'imperial'  # Use 'metric' for Celsius
        }
    elif forecast_type == 'forecast':
        url = 'http://api.openweathermap.org/data/2.5/forecast'
        params = {
            'q': city_or_zip,
            'appid': API_KEY,
            'units': 'imperial'
        }
    else:
        print("Invalid forecast type")
        sys.exit(1)
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data (Status code: {response.status_code})")
        sys.exit(1)

def display_current_weather(data):
    city = data['name']
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    temp_feel = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    pressure = data['main']['pressure']
    sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
    sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')

    print(f"City: {city}")
    print(f"Weather: {weather.capitalize()}")
    print(f"Temperature: {temp}°F")
    print(f"Feels Like: {temp_feel}°F")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} mph")
    print(f"Pressure: {pressure} hPa")
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")

def display_forecast(data):
    print("5-Day Forecast:")
    for item in data['list']:
        dt = datetime.datetime.fromtimestamp(item['dt'])
        weather = item['weather'][0]['description']
        temp = item['main']['temp']
        print(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} - Weather: {weather.capitalize()}, Temperature: {temp}°F")

def main():
    if len(sys.argv) < 2:
        print("Usage: python weather_app.py [city_name or zip_code] [current/forecast]")
        sys.exit(1)

    city_or_zip = sys.argv[1]
    forecast_type = sys.argv[2] if len(sys.argv) == 3 else 'current'
    
    if forecast_type == 'current':
        weather_data = get_weather_data(city_or_zip, forecast_type)
        display_current_weather(weather_data)
    elif forecast_type == 'forecast':
        weather_data = get_weather_data(city_or_zip, forecast_type)
        display_forecast(weather_data)
    else:
        print("Invalid forecast type. Choose 'current' or 'forecast'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
