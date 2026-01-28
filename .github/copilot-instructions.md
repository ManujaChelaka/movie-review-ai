# AI Coding Guidelines for Movie Review AI

## Project Overview
Movie Review AI is a Flask-based sentiment analysis application that fetches real movie reviews from The Movie Database (TMDB) API and performs sentiment analysis. The frontend (HTML/JS) communicates with a Python backend via REST API on port 5000.

**Architecture**: Frontend (Static HTML/JS) ↔ Flask Backend ↔ TMDB API  
**Key Pattern**: Query-based analysis (movie title input) → Real reviews fetched → Sentiment scores calculated → Results displayed

## Critical Setup Requirements

### Backend Dependencies
- **`requirements.txt` is currently empty** - Must install manually:
  - `flask` - Web server
  - `flask-cors` - Enable cross-origin requests  
  - `requests` - HTTP calls to TMDB API
  - `vaderSentiment` - Sentiment analysis
  - `beautifulsoup4` - HTML parsing (for scraper.py)

- **TMDB API Token**: Required in `Backend/app.py` line 11 as `TMDB_TOKEN = "YOUR_TOKEN_HERE"` - this MUST be set before the `/analyze` endpoint works

### Running the Application
1. Start Flask backend: `python Backend/app.py` (runs on `http://127.0.0.1:5000`)
2. Open `Frontend/index.html` in browser
3. The frontend calls `http://127.0.0.1:5000/analyze?title={movieTitle}` when user clicks "Search & Analyze"

## Data Flow & API Contract

### Backend Endpoint: `/analyze` (GET)
- **Input**: `?title=MovieTitle` query parameter (defaults to "Inception")
- **Output** JSON structure (critical - Frontend expects exact keys):
  ```json
  {
    "total_reviews": number,
    "positive": number,
    "negative": number,
    "overall_sentiment": "Positive"|"Negative",
    "detailed_results": [{"text": string, "sentiment": "POSITIVE"|"NEGATIVE", "confidence": number}]
  }
  ```
- **Note**: Frontend code references `data.ai_summary` and `data.neutral` but backend doesn't return these - indicates potential mismatch

### Sentiment Scoring
- VADER analyzer returns compound score (-1 to 1)
- Score ≥ 0.05 → POSITIVE, otherwise NEGATIVE
- Takes only first 5 reviews to avoid performance issues

## Project Conventions & Patterns

1. **CORS enabled** - Frontend on different port than backend requires `CORS()` setup
2. **Error handling**: `/analyze` returns 404 if no reviews found; Frontend expects `response.ok` check
3. **Chart management**: `myChart.destroy()` required before redrawing to prevent glitches
4. **Review truncation**: Long reviews truncated to 200 chars in results display
5. **Sentiment categories**: Only POSITIVE/NEGATIVE (no NEUTRAL in backend, but UI expects 3 categories)

## Key Files Reference

- [Backend/app.py](Backend/app.py) - Flask server, TMDB API integration, VADER sentiment analysis
- [Backend/scraper.py](Backend/scraper.py) - Local HTML parsing utility (currently unused in main flow)
- [Frontend/script.js](Frontend/script.js) - Fetch logic, chart rendering, state management
- [Frontend/index.html](Frontend/index.html) - UI layout with Chart.js visualization

## Common Issues & Debugging

- **"Backend server not running!"** - Flask must be started; check port 5000 not in use
- **API token 401 error** - TMDB_TOKEN not set or invalid
- **No reviews found** - Movie title may not exist in TMDB; try popular movies (Inception, Batman, etc.)
- **Chart not updating** - Ensure previous chart instance destroyed before creating new one
- **CORS errors** - Verify `CORS(app)` initialization in app.py

## Before Making Changes

- Verify both frontend and backend JSON/response field names match (currently inconsistencies with `ai_summary`, `neutral`)
- Update `requirements.txt` when adding dependencies
- Test TMDB API token before assuming endpoint issues
- Keep 5-review limit for performance
