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

## How it Works

User Input → Sentiment Analysis → Recommendation Output
<img width="1880" height="791" alt="Screenshot 2026-04-22 131405" src="https://github.com/user-attachments/assets/27340a6b-f8b2-4482-8137-5ad7a0e29f07" />
<img width="1889" height="1037" alt="Screenshot 2026-04-22 131427" src="https://github.com/user-attachments/assets/26dfa0e7-56ef-4ce2-82d2-cf4fa1aca3a9" />

This API takes user text as input, analyzes the sentiment using NLP, and returns mood-based content recommendations.


## 👩‍💻 Author
Roshni K  
GitHub: https://github.com/Rosiverse
