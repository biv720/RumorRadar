import os
from dotenv import load_dotenv

load_dotenv()

# Kafka
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "rumorradar")

# Risk thresholds
RISK_THRESHOLD = int(os.getenv("RISK_THRESHOLD", 70))

# App config
ENV = os.getenv("ENV", "development")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
