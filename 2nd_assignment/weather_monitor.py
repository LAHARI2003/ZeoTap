import requests
import time
import sqlite3
from datetime import datetime
from db_handler import create_connection, insert_weather_data, calculate_daily_summary
from alerts import check_alerts
from visualizations import generate_visualization
from db_handler import create_connection, create_table, insert_weather_data, calculate_daily_summary


API_KEY = "37852acb4b0a98f1e8e360c916edbe39"  # Replace with your OpenWeatherMap API key
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
INTERVAL = 300  # 5 minutes

def fetch_weather_data(city):
    """Fetch weather data from OpenWeatherMap API"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code} - {response.text}")
        return None

def kelvin_to_celsius(temp_kelvin):
    """Convert temperature from Kelvin to Celsius"""
    return temp_kelvin - 273.15

def process_weather_data(weather_data, city):
    """Process and return weather data"""
    temp = kelvin_to_celsius(weather_data['main']['temp'])
    feels_like = kelvin_to_celsius(weather_data['main']['feels_like'])
    condition = weather_data['weather'][0]['main']
    timestamp = weather_data['dt']
    date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

    return (city, temp, feels_like, condition, timestamp, date)

def run_weather_monitor():
    conn = create_connection("weather_data.db")
    create_table(conn)
    
    while True:
        for city in CITIES:
            weather_data = fetch_weather_data(city)
            if weather_data:
                processed_data = process_weather_data(weather_data, city)
                insert_weather_data(conn, processed_data)
                check_alerts(conn, processed_data)
        
        calculate_daily_summary(conn)
        generate_visualization(conn)
        time.sleep(INTERVAL)

if __name__ == "__main__":
    run_weather_monitor()
