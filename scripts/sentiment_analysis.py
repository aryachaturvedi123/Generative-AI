from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    return round(blob.sentiment.polarity, 2), round(blob.sentiment.subjectivity, 2)

def analyze_sentiment(text):
    # Simple dummy logic, replace with your ML model later
    if "hurt" in text or "reckless" in text:
        sentiment = "left"
    elif "support" in text or "growth" in text:
        sentiment = "right"
    else:
        sentiment = "neutral"

    polarity, subjectivity = get_sentiment(text)
    return sentiment, polarity, subjectivity

