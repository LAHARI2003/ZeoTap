import sqlite3

def create_connection():
    """Create a database connection to the SQLite database."""
    conn = sqlite3.connect('weather_data.db')  # This will create the file if it doesn't exist
    return conn

def create_table(conn):
    """Create the daily_weather table if it doesn't already exist."""
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS daily_weather (
                id INTEGER PRIMARY KEY,
                date TEXT UNIQUE,
                avg_temp REAL,
                max_temp REAL,
                min_temp REAL,
                dominant_condition TEXT
            )
        ''')
