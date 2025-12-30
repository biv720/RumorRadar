from kafka import KafkaConsumer
from config.settings import KAFKA_BROKER, KAFKA_TOPIC, RISK_THRESHOLD
from consumer.analyzer import analyze_text
from consumer.risk_engine import calculate_risk
from consumer.alerts import send_alert

def start_consumer():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        auto_offset_reset="earliest",
        value_deserializer=lambda x: x.decode("utf-8")
    )

    print("🛰️ RumorRadar is live...")

    for msg in consumer:
        text = msg.value
        print(f"\n📩 Incoming: {text}")

        analysis = analyze_text(text)
        risk = calculate_risk(
            analysis["sentiment"],
            analysis["keywords"]
        )

        print(f"🧠 Sentiment: {analysis['sentiment']}")
        print(f"🔎 Keywords: {analysis['keywords']}")
        print(f"⚠️ Risk: {risk}")

        if risk["score"] >= RISK_THRESHOLD:
            send_alert(text, risk)
