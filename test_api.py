import requests

API_KEY = "37852acb4b0a98f1e8e360c916edbe39"  # Replace with your API key
CITIES = ["Delhi"]

def fetch_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error fetching data for {city}: {response.status_code} - {response.text}")

for city in CITIES:
    fetch_weather_data(city)
