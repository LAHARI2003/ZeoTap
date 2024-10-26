import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("SQLite connection established.")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """Create the weather table if it doesn't exist"""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            temp REAL NOT NULL,
            feels_like REAL NOT NULL,
            condition TEXT NOT NULL,
            timestamp INTEGER NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()


def insert_weather_data(conn, data):
    """Insert weather data into the database."""
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather (city, temp, feels_like, condition, timestamp, date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()

def calculate_daily_summary(conn):
    """Calculate daily summaries by averaging temperatures."""
    cursor = conn.cursor()
    query = '''
        SELECT city, date, AVG(temp) as avg_temp, MAX(temp) as max_temp, MIN(temp) as min_temp, condition
        FROM weather
        GROUP BY city, date
    '''
    cursor.execute(query)
    return cursor.fetchall()
