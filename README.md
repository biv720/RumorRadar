# 🛰️ RumorRadar — Real-Time Misinformation Detection System

<div align="center">

![RumorRadar Banner](https://media.discordapp.net/attachments/758945965939359745/1455270964274266134/image.png?ex=69541e33&is=6952ccb3&hm=ba667225ee6eaa9b8a8e256d6b9bd6f20fd422cd2e515b6a336330cb6bb0b317&=&format=webp&quality=lossless&width=1451&height=367)

**A real-time misinformation monitoring and alerting system built using Kafka, Python, and NLP. Analyzes streaming text data to detect potential rumors, emotionally charged narratives, and emerging misinformation trends with explainable alerts.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Kafka](https://img.shields.io/badge/Apache%20Kafka-Streaming-orange.svg)](https://kafka.apache.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Development-yellow.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## ⚠️ Project Status

**🟡 Actively under development**

Some features are limited due to API rate limits and compute constraints. See [Limitations](#️-important-note-limitations) for details.

---

## 🚀 Features

### ✅ Real-Time Message Processing
- Kafka-based streaming architecture
- Handles high-throughput message ingestion
- Designed to scale horizontally

### 🧠 NLP-Powered Analysis
- Sentiment analysis for emotional tone detection
- Keyword & pattern-based filtering
- Early-stage misinformation signal detection

### 📈 Trend & Risk Detection
- Detects sudden spikes in sensitive keywords
- Flags emotionally charged or fear-inducing content
- Assigns risk levels to messages

### 🚨 Alerting System
- Real-time alerts for suspicious content
- Desktop notifications
- Console-based live monitoring

### 🔍 Explainable Output

Each alert includes:
- ✅ Triggered keywords
- ✅ Sentiment score
- ✅ Reason for flagging
- ✅ Risk classification

---

## 🧩 System Architecture

```
┌──────────────┐
│ Data Source  │
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│ Kafka Producer   │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Kafka Consumer   │
└──────┬───────────┘
       │
       ▼
┌──────────────────────────┐
│ NLP + Risk Analysis      │
│ Engine                   │
└──────┬───────────────────┘
       │
       ▼
┌──────────────────┐
│ Alert System     │
└──────┬───────────┘
       │
       ▼
┌──────────────────────────┐
│ Live Monitoring /        │
│ Dashboard                │
└──────────────────────────┘
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python |
| **Streaming** | Apache Kafka |
| **NLP** | TextBlob (currently) |
| **Alerts** | Plyer + system notifications |
| **Architecture** | Event-driven, scalable |
| **Future Scope** | ML-based classification, dashboard UI |

---

## 📊 Current Capabilities

| Feature | Status |
|---------|--------|
| Kafka-based streaming | ✅ Complete |
| Keyword detection | ✅ Complete |
| Sentiment analysis | ✅ Complete |
| Alert system | ✅ Complete |
| Risk scoring | ⚙️ In progress |
| Trend detection | ⚙️ In progress |
| Dashboard UI | 🛠 Planned |
| ML-based rumor detection | 🛠 Planned |

---

## ▶️ Getting Started

### Prerequisites

- Python 3.8+
- Apache Kafka (running locally or remotely)
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/biv720/rumorradar.git
   cd rumorradar
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Kafka**
   - Start Zookeeper:
     ```bash
     bin/zookeeper-server-start.sh config/zookeeper.properties
     ```
   - Start Kafka:
     ```bash
     bin/kafka-server-start.sh config/server.properties
     ```

4. **Run the system**
   ```bash
   python main.py
   ```

---

## 🧪 Why This Project Exists

> **Misinformation spreads faster than verification.**

RumorRadar aims to:
- ✅ Detect rumor formation early
- ✅ Provide explainable alerts
- ✅ Assist in analyzing information flow
- ✅ Act as a foundation for responsible AI-based monitoring tools

This project is built with **scalability**, **transparency**, and **ethical AI principles** in mind.

---

## ⚠️ Important Note (Limitations)

This project is currently under **active development**.

Due to:
- API rate limits
- Compute constraints
- Free-tier infrastructure

Some features (such as large-scale message ingestion, advanced ML inference, and long-term trend analysis) are **intentionally limited** in the current version.

These constraints are **documented** and will be addressed in future iterations.

---

## 🧭 Roadmap

- [ ] Add trend-based rumor scoring
- [ ] Implement message clustering
- [ ] Add web-based dashboard
- [ ] Improve NLP with transformer models (BERT/RoBERTa)
- [ ] Visualize misinformation spread patterns
- [ ] Deploy scalable cloud version (AWS/GCP)
- [ ] Integrate graph-based analysis
- [ ] Add multi-language support

---

## 🤝 Contributing

Contributions are welcome! This project is open to improvements and new ideas.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Bivraj** — Computer Science Engineer | AI & Systems Enthusiast

Focused on:
- AI-driven systems
- Real-time data processing
- Ethical and explainable AI
- Scalable backend architectures

[![GitHub](https://img.shields.io/badge/GitHub-biv720-black?logo=github)](https://github.com/biv720)

---

## 📌 Disclaimer

This project is intended for **educational and research purposes only**. 

⚠️ It does not claim to identify factual truth and should **not be used as a sole decision-making system** for content moderation or fact-checking.

The system provides signals and insights, but human judgment and verification remain essential.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with 🧠 for a more transparent information ecosystem**

[⭐ Star this repo](https://github.com/biv720/rumorradar) | [🐛 Report Bug](https://github.com/biv720/rumorradar/issues) | [✨ Request Feature](https://github.com/biv720/rumorradar/issues)

</div>
