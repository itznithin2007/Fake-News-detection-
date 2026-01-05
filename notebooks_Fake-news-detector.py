# Fake News Detector 

def fake_news_detector(news):

    # Convert to lowercase
    news = news.lower()

    # List of suspicious words (fake indicators)
    fake_words = [
        "shocking", "unbelievable", "miracle", "secret",
        "you won't believe", "breaking", "viral",
        "click here", "guaranteed", "exposed"
    ]

    # List of real news words
    real_words = [
        "government", "official", "report", "according",
        "data", "minister", "statement", "confirmed"
    ]

    fake_score = 0
    real_score = 0

    # Check fake words
    for word in fake_words:
        if word in news:
            fake_score += 1

    # Check real words
    for word in real_words:
        if word in news:
            real_score += 1

    # Check excessive punctuation
    if "!!!" in news or "???" in news:
        fake_score += 1

    # Final decision
    if fake_score > real_score:
        return "FAKE NEWS"
    else:
        return "REAL NEWS"


# -------------------------------
# Main Program
# -------------------------------

print("Fake News Detector (Pure Python)")
print("--------------------------------")

news_input = input("Enter news text:\n")

result = fake_news_detector(news_input)

print("\nResult:", result)