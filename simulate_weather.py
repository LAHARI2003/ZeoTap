import sqlite3
from datetime import datetime, timedelta
import random

# Function to establish SQLite connection
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("SQLite connection established.")
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

# Function to insert weather data into the database
def insert_weather_data(conn, city, temp, feels_like, condition, date):
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current timestamp
    
    cursor.execute('''
        INSERT INTO weather (city, temp, feels_like, condition, date, timestamp) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (city, temp, feels_like, condition, date, timestamp))  # Add timestamp to query
    
    conn.commit()
    print(f"Data inserted for {city} on {date} with timestamp {timestamp}")

# Function to simulate weather updates for a given number of days
def simulate_weather_updates(conn, cities, start_date, days):
    conditions = ["Sunny", "Cloudy", "Rainy", "Stormy"]
    
    for day in range(days):
        current_date = start_date + timedelta(days=day)
        
        for city in cities:
            # Randomly generate temperature and weather condition
            temp = random.uniform(20.0, 40.0)  # Example: 20°C to 40°C
            feels_like = temp + random.uniform(-2.0, 2.0)  # Slight variation for feels like
            condition = random.choice(conditions)  # Random weather condition

            # Insert weather data for the city
            insert_weather_data(conn, city, temp, feels_like, condition, current_date)
        
        print(f"Weather data simulated for {current_date}")
    
    print("Weather simulation completed.")

# Main function to run the weather simulation
def run_simulation():
    database = "weather_data.db"
    
    # Cities to simulate
    cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
    
    # Connect to the database
    conn = create_connection(database)
    
    # Start date and number of days for the simulation
    start_date = datetime(2024, 1, 1)
    days = 10  # Simulate 10 days of data
    
    if conn:
        simulate_weather_updates(conn, cities, start_date, days)
        conn.close()
        print("SQLite connection closed.")

if __name__ == "__main__":
    run_simulation()
