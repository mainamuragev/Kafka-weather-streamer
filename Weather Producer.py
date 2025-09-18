import requests
from kafka import KafkaProducer
import time
import json

# OpenWeather API setup
API_KEY = 'af83b437f52e300db0316ff1e84f837a'  # Replace with your actual API key
CITY = 'Nairobi'
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

#  Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def fetch_weather():
    """Fetch current weather data from OpenWeather API."""
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()
        weather = {
            'city': CITY,
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'condition': data['weather'][0]['description'],
            'timestamp': time.time()
        }
        return weather
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return None

# Stream weather data every 60 seconds
while True:
    weather_data = fetch_weather()
    if weather_data:
        producer.send('weather_logs', value=weather_data)
        print(f"Sent: {weather_data}")
    time.sleep(60)