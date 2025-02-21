from flask import Flask, request, render_template
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize Flask app
app = Flask(__name__)

# Initialize Sentiment Analyzer
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

# Homepage Route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        result = analyze_sentiment(text)
        return render_template("index.html", text=text, result=result)
    return render_template("index.html", text="", result="")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
