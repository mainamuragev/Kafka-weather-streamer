from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'weather_logs',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for msg in consumer:
    data = msg.value
    print(f"{data['city']} | {data['temp']}°C | {data['humidity']}% | {data['condition']}")
