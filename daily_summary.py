def get_daily_weather_summary(conn):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT city, date,
               AVG(temp) as avg_temp,
               MAX(temp) as max_temp,
               MIN(temp) as min_temp,
               mode() WITHIN GROUP (ORDER BY condition) as dominant_condition
        FROM weather
        GROUP BY city, date
    ''')
    return cursor.fetchall()

def process_daily_summary(conn):
    cursor = conn.cursor()
    cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

    for city in cities:
        cursor.execute("""
            SELECT AVG(temp), MAX(temp), MIN(temp)
            FROM weather WHERE city = ?
        """, (city,))
        avg_temp, max_temp, min_temp = cursor.fetchone()
        
        print(f"Summary for {city}:")
        print(f"Average Temperature: {avg_temp:.2f}°C")
        print(f"Maximum Temperature: {max_temp:.2f}°C")
        print(f"Minimum Temperature: {min_temp:.2f}°C")
        
    print("Daily summaries processed successfully.")
