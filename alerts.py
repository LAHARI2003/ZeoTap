def check_alerts(conn, data):
    city, temp, feels_like, condition, timestamp = data
    threshold_temp = 35.0
    
    if temp > threshold_temp:
        print(f"ALERT: Temperature exceeded threshold in {city}! Current temperature: {temp:.2f}°C")
    else:
        print(f"No alerts for {city} on {timestamp}.")
