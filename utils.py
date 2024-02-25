import requests
from datetime import datetime, timedelta

# followinf are all the necessar business logic functions as well as API fetching function defined
# Fetch external weather data
def get_weather(city, country):
    api_key = '1c920b545ed61c6a7d652acbe892024a'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"

def simulate_drying(turf_type):
    if turf_type == 'Natural':
        drying_time = 36
    elif turf_type == 'Artificial':
        drying_time = 12
    elif turf_type == 'Hybrid':
        drying_time = 24

    return drying_time

def calculate_health_score(rain_duration, turf_type, city, country):
    if turf_type == 'Natural':
        cycle_duration = 3
    elif turf_type == 'Artificial':
        cycle_duration = 6
    elif turf_type == 'Hybrid':
        cycle_duration = 4

    cycles = rain_duration // cycle_duration
    health_score = 10 - (cycles * 2)

    # Fetch weather data
    weather_data = get_weather(city, country)
    if 'rain' in weather_data:
        rain_duration = weather_data['rain']['1h'] / 3600  # Convert rain volume from mm to hours
        cycles = rain_duration // cycle_duration
        health_score -= (cycles * 2)

    return max(health_score, 0)

def schedule_maintenance(last_maintenance_date, health_score, turf_type):
    if health_score < 10:
        if turf_type == 'Natural':
            drying_time = 36
        elif turf_type == 'Artificial':
            drying_time = 12
        elif turf_type == 'Hybrid':
            drying_time = 24

        maintenance_date = last_maintenance_date + timedelta(hours=drying_time)
        return maintenance_date
    else:
        return None

def schedule_replacement(health_score):
    if health_score == 2:
        replacement_date = datetime.now() + timedelta(days=30)
        return replacement_date
    else:
        return None
