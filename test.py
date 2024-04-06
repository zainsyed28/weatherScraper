import pyowm
from datetime import datetime, timedelta

owm = pyowm.OWM('d7bbe8c738c15cc7bb21e38a262f5bf1')  # Replace with your actual API key
weather_mgr = owm.weather_manager()
place = 'Los Angeles, US'
observation = weather_mgr.weather_at_place(place)
temperature = observation.weather.temperature("fahrenheit")["temp"]
humidity = observation.weather.humidity
wind = observation.weather.wind()
print(f'Temperature: {temperature}°F')
print(f'Humidity: {humidity}%')
print(f'Wind Speed: {wind["speed"]} m/s')