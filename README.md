#  Nairobi Weather Stream

A real-time weather streaming pipeline built with Python and Apache Kafka. It fetches live weather data from OpenWeather, streams it into a Kafka topic (`weather_logs`), and logs each entry locally for analysis or visualization.

---

##  Project Structure



---

##   How It Works

- `weather_producer.py`: Fetches weather data from OpenWeather every 60 seconds and sends it to Kafka.
- `weather_consumer.py`: Listens to the `weather_logs` topic and logs each message to both the terminal and `weather_log.txt`.
- Kafka auto-creates the topic if it doesn’t exist.
- Designed for reproducibility, telemetry, and local analysis from Nairobi.

---

##  Setup Instructions

### 1. CLONE 

 ##Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

##Install Dependencies
pip install -r requirements.txt --break-system-packages

##Start Kafka Locally
# Terminal 1: Start Zookeeper
~/kafka/bin/zookeeper-server-start.sh ~/kafka/config/zookeeper.properties

# Terminal 2: Start Kafka Broker
~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties

##Run the Pipeline
Producer
python3 python_modules/weather_producer.py

Consumer
python3 python_modules/weather_consumer.py

Sample Output
2025-09-18T06:15:23 | Nairobi | 21.7°C | 72% | scattered clouds

Log File (weather_log.txt):
2025-09-18T06:15:23 | Nairobi | 21.7°C | 72% | scattered clouds

## Local Relevance
Built and tested in Nairobi, Kenya—this project showcases how global APIs and open-source tools can be locally adapted

##Dependencies
- kafka-python
- requests

Built by Maina Murage — mechanical engineer pivoting into software/data engineering. Passionate about smart infrastructure, reproducible workflows.









