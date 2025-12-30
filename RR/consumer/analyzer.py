from textblob import TextBlob

TRIGGER_KEYWORDS = [
    "fake",
    "scam",
    "nuclear",
    "attack",
    "collapse",
    "fraud",
    "breaking"
]

def analyze_text(text: str):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    matched_keywords = [
        word for word in TRIGGER_KEYWORDS
        if word.lower() in text.lower()
    ]

    return {
        "sentiment": sentiment,
        "keywords": matched_keywords
    }
