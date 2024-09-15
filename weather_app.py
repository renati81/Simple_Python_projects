import requests 
import sys
import datetime

# Replace with your OpenWeatherMap API key
# Go to OpenWeatherMap and create an account in API key you can find the key or else you can create your own key
API_KEY = 'Give your openWeather API key'

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
    print(f"5-Day Forecast of {city}:")
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


# To run this code open the cmd prompt and save the python code file in the desktop then give %userprofile%/desktop + enter + dir, it will display all the files located 
# in the desktop, now we can see the file that you have saved with the code.
# 1) For current forecast type input 'python your_file_name.py [city or zip]
# EX: python weather_app.py "new york"
# output:
# City: New York
# Weather: Clear sky
# Temperature: 85.4°F
# Feels Like: 88.2°F
# Humidity: 60%
# Wind Speed: 5 mph
# Pressure: 1010 hPa
# Sunrise: 2024-09-15 06:32:12
# Sunset: 2024-09-15 19:45:23
# 2) For 5-day forecast type input 'python your_file_name.py [city or zip] forecast
# Ex: python weather_app.py "new york" forecast
#5-Day Forecast of New York:
#2024-09-15 19:00:00 - Weather: Clear sky, Temperature: 70.74°F
#2024-09-15 22:00:00 - Weather: Clear sky, Temperature: 70.2°F
#2024-09-16 01:00:00 - Weather: Scattered clouds, Temperature: 68.68°F
#2024-09-16 04:00:00 - Weather: Overcast clouds, Temperature: 66.42°F
#2024-09-16 07:00:00 - Weather: Overcast clouds, Temperature: 66.52°F
#.......
#2024-09-20 13:00:00 - Weather: Overcast clouds, Temperature: 78.62°F
#2024-09-20 16:00:00 - Weather: Overcast clouds, Temperature: 77.49°F

