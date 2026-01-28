import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)

# Use your actual TMDB Read Access Token here
TMDB_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNDcyNmE1NDVmYTUwMGNiNGRlOTE0ZDUxMGM1NThjMSIsIm5iZiI6MTc2MTQ4NTkyNS42MDQsInN1YiI6IjY4ZmUyNDY1ZDQxMzc3YjM5ZDkyNzA5OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.EcTaKTqxhkU7ESdkq0VlzAh5qdU45QpXhHvvgUb8YnM"

HEADERS = {
    "Authorization": f"Bearer {TMDB_TOKEN}",
    "accept": "application/json"
}

def get_real_reviews(movie_title):
    # Search for movie ID and poster
    search_url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}"
    res = requests.get(search_url, headers=HEADERS).json()
    if not res.get('results'): return [], None
    
    movie_id = res['results'][0]['id']
    poster_path = res['results'][0].get('poster_path')
    
    # Fetch reviews
    rev_url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews"
    rev_res = requests.get(rev_url, headers=HEADERS).json()
    reviews = [r['content'] for r in rev_res.get('results', [])]
    return reviews, poster_path

@app.route("/analyze", methods=["GET"])
def analyze_movie():
    title = request.args.get('title', 'Inception')
    poster_url = None
    
    if TMDB_TOKEN == "YOUR_TOKEN_HERE" or not TMDB_TOKEN:
        # Fallback to dummy data
        reviews = [
            "Amazing movie with stunning visuals",
            "Story was weak and boring",
            "Actors did a great job",
            "Too long and poorly edited",
            "Enjoyable but not memorable"
        ]
    else:
        reviews, poster_path = get_real_reviews(title)
        if poster_path:
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    
    if not reviews:
        return jsonify({"error": "No reviews found"}), 404

    analyzer = SentimentIntensityAnalyzer()
    results = []
    for text in reviews[:5]:
        score = analyzer.polarity_scores(text)['compound']
        results.append({
            "text": text[:200] + "...",
            "sentiment": "POSITIVE" if score >= 0.05 else "NEGATIVE",
            "confidence": round(abs(score) * 100, 1)
        })

    pos = len([r for r in results if r['sentiment'] == "POSITIVE"])
    neg = len(results) - pos
    
    return jsonify({
        "total_reviews": len(reviews),
        "positive": pos,
        "negative": neg,
        "neutral": 0, # Added neutral for frontend
        "overall_sentiment": "Positive" if pos >= (len(results)/2.0) else "Negative",
        "ai_summary": "The overall consensus is " + ("Positive" if pos >= (len(results)/2.0) else "Negative"), # Added ai_summary
        "poster_url": poster_url, # Added poster_url
        "detailed_results": results
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)