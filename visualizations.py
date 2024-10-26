import matplotlib.pyplot as plt
from datetime import datetime

def generate_visualization(conn):
    """Generate temperature summary visualization."""
    cursor = conn.cursor()
    query = '''
        SELECT city, date, AVG(temp) as avg_temp
        FROM weather
        GROUP BY city, date
    '''
    cursor.execute(query)
    results = cursor.fetchall()

    # Organize data by city
    temperature_data = {}
    for row in results:
        city, date, avg_temp = row
        if city not in temperature_data:
            temperature_data[city] = {'dates': [], 'avg_temps': []}
        temperature_data[city]['dates'].append(date)
        temperature_data[city]['avg_temps'].append(avg_temp)

    # Plot data
    plt.figure(figsize=(10, 5))
    for city, temps in temperature_data.items():
        dates = [datetime.strptime(date, "%Y-%m-%d") for date in temps['dates']]
        avg_temps = temps['avg_temps']
        plt.plot(dates, avg_temps, label=city)

    plt.title('Daily Average Temperature')
    plt.xlabel('Date')
    plt.ylabel('Average Temperature (°C)')
    plt.legend(loc="best")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
