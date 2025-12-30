from plyer import notification
from datetime import datetime

def send_alert(message, risk_data):
    alert_msg = (
        f"Risk Level: {risk_data['level']}\n"
        f"Score: {risk_data['score']}\n"
        f"Message: {message}"
    )

    print("\n🚨 ALERT 🚨")
    print(alert_msg)
    print("-" * 50)

    notification.notify(
        title="RumorRadar Alert",
        message=alert_msg,
        timeout=5
    )

    # Log to file
    with open("logs/alerts.log", "a") as f:
        f.write(f"[{datetime.now()}] {alert_msg}\n")
