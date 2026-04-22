# SentixFlow – AI-Based Recommendation Backend

## 🚀 Overview
SentixFlow is a backend system that analyzes user sentiment and recommends media content based on their mood. It uses NLP techniques and integrates external APIs to deliver personalized results.

---

## 🔧 Features
- Analyze user sentiment from input text
- Generate mood-based content recommendations
- REST API endpoints for processing and retrieval
- Integration with YouTube Data API
- Fast and scalable backend architecture

---

## 🛠 Tech Stack
- Python
- FastAPI
- NLP (Text Processing)
- YouTube Data API
- SQLite / PostgreSQL

---

## 🔗 API Endpoints

### POST /analyze
- Analyzes user sentiment

### GET /recommend
- Returns content recommendations based on mood

---

## 📌 Future Improvements
- Add user authentication system
- Improve recommendation accuracy
- Deploy backend to cloud platform

---
## Example Request

POST /analyze

{
  "text": "I feel happy today"
}

## Example Response

{
  "sentiment": "positive",
  "recommendation": "watch motivational videos"
}

--- 


## 👩‍💻 Author
Roshni K  
GitHub: https://github.com/Rosiverse
