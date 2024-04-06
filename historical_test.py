import pyowm
from datetime import datetime, timedelta

owm = pyowm.OWM('')  # Replace with your actual API key
weather_mgr = owm.weather_manager()
place = 'Los Angeles, US'

# Date range: from 2011-01-01 to today
start_date = '2021-01-01'
end_date = '2021-01-31'
history = weather_mgr.weather_history_at_place(place, start_date, end_date)