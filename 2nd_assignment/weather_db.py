import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("SQLite connection established.")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create a table for storing daily weather summaries."""
    try:
        sql_create_weather_table = """
        CREATE TABLE IF NOT EXISTS daily_weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            city TEXT NOT NULL,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT,
            UNIQUE(date, city)
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_weather_table)
        print("Weather table created or already exists.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def save_daily_summary(conn, date, avg_temp, max_temp, min_temp, dominant_condition):
    """Insert or update a daily weather summary for a city."""
    try:
        sql_insert_summary = """
        INSERT INTO daily_weather (date, city, avg_temp, max_temp, min_temp, dominant_condition)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(date, city) DO UPDATE SET
            avg_temp=excluded.avg_temp,
            max_temp=excluded.max_temp,
            min_temp=excluded.min_temp,
            dominant_condition=excluded.dominant_condition;
        """
        cursor = conn.cursor()
        for city in ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]:
            cursor.execute(sql_insert_summary, (date, city, avg_temp, max_temp, min_temp, dominant_condition))
        conn.commit()
        print("Daily summary inserted/updated successfully.")
    except sqlite3.Error as e:
        print(f"Error saving daily summary: {e}")

if __name__ == "__main__":
    # For testing purposes, you can create a connection here
    conn = create_connection("weather_data.db")
    create_table(conn)
    if conn:
        conn.close()
