import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the Sentiment Analyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    score = sia.polarity_scores(text)
    if score['compound'] >= 0.05:
        return "Positive 😀"
    elif score['compound'] <= -0.05:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# User input loop
while True:
    user_input = input("\nEnter a sentence (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    print("Sentiment:", analyze_sentiment(user_input))
