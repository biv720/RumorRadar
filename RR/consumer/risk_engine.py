def calculate_risk(sentiment, keywords):
    score = 0

    # Sentiment weight
    if sentiment < -0.3:
        score += 30
    elif sentiment > 0.3:
        score += 10

    # Keyword weight
    score += len(keywords) * 15

    # Final clamp
    score = min(score, 100)

    if score >= 70:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "score": score,
        "level": level
    }
