from flask import Flask, request, jsonify, send_file
import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import urllib.parse

app = Flask(__name__)

# Load dataset
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")
credits.columns = ["id", "title", "cast", "crew"]

df = movies.merge(credits, on="id")

# Extract genre names
def extract_names(text):
    try:
        return " ".join([i["name"] for i in ast.literal_eval(text)])
    except:
        return ""

df["genres"] = df["genres"].apply(extract_names)

# Combine text features
df["combined"] = (
    df["overview"].fillna("") + " " +
    df["tagline"].fillna("") + " " +
    df["keywords"].fillna("") + " " +
    df["genres"].fillna("")
)

# Map genres to moods
def genre_to_mood(genres):
    genres = genres.lower()
    if "romance" in genres:
        return "romantic"
    if "comedy" in genres:
        return "happy"
    if "drama" in genres:
        return "sad"
    if "horror" in genres or "thriller" in genres:
        return "scared"
    if "action" in genres:
        return "angry"
    return "neutral"

df["mood_label"] = df["genres"].apply(genre_to_mood)

# Train Naive Bayes model
tfidf = TfidfVectorizer(stop_words="english")
X = tfidf.fit_transform(df["combined"])
y = df["mood_label"]

model = MultinomialNB()
model.fit(X, y)

# Generate search link dynamically
def get_movie_link(title, platform="google"):
    query = urllib.parse.quote(title + " movie")
    if platform == "google":
        return f"https://www.google.com/search?q={query}"
    elif platform == "youtube":
        return f"https://www.youtube.com/results?search_query={query}+trailer"
    else:
        return "#"

# Recommend movies
def recommend_movies(predicted_mood):
    subset = df[df["mood_label"] == predicted_mood]
    if subset.empty:
        return []
    sample = subset.sample(min(10, len(subset)))
    return [{"title": row["title_x"], "link": get_movie_link(row["title_x"], "youtube")} for _, row in sample.iterrows()]

# Routes
@app.route("/")
def home():
    return send_file("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        if request.is_json:
            mood_text = request.get_json().get("mood", "").strip()
        else:
            mood_text = request.form.get("mood", "").strip()

        if not mood_text:
            return jsonify({"error": "Please enter a mood."}), 400

        # Predict mood
        mood_vector = tfidf.transform([mood_text])
        predicted_mood = model.predict(mood_vector)[0]

        # Recommend movies
        result = recommend_movies(predicted_mood)
        if not result:
            return jsonify({
                "predicted_mood": predicted_mood,
                "recommendations": [],
                "message": "No movies found for this mood."
            })

        return jsonify({"predicted_mood": predicted_mood, "recommendations": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
