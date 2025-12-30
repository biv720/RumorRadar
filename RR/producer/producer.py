import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kafka import KafkaProducer
from config.settings import KAFKA_BROKER, KAFKA_TOPIC
import time

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: v.encode("utf-8")
)

print("📡 Producer started...")

messages = [
    "Breaking: Bank collapse expected soon",
    "This looks like fake news",
    "Markets are stable today",
    "Nuclear threat rising",
    "Possible scam detected"
]

while True:
    for msg in messages:
        print(f"➡️ Sending: {msg}")
        producer.send(KAFKA_TOPIC, msg)
        producer.flush()
        time.sleep(2)
