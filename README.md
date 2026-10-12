<div align="center">

# 🎬 Movie Review AI
### AI-Powered Movie Review Sentiment & Analytics Platform

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-API-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

<p align="center">
  An AI-powered Movie Review Analyser that collects, processes, and analyzes movie reviews using Natural Language Processing (NLP) techniques to generate sentiment insights, ratings, and summary analytics through an interactive web interface.
</p>

[Overview](#-overview) • [Key Features](#-key-features) • [Repository Structure](#-repository-structure) • [Tech Stack](#-tech-stack) • [Getting Started](#-getting-started) • [NLP Pipeline](#-nlp--sentiment-analysis-pipeline)

</div>

---

## 📖 Overview

**Movie Review AI** (`movie-review-ai`) is a full-stack Natural Language Processing (NLP) web application designed to evaluate audience reception and classify unstructured movie review text into actionable sentiment metrics. 

By pairing a Python-driven machine learning `Backend` with a responsive `Frontend` web interface (HTML, CSS, JavaScript) and interactive analytics dashboard, the system performs real-time text preprocessing, polarity classification (Positive / Negative / Neutral), confidence scoring, and aggregated rating generation.

---

## ✨ Key Features

* **🧠 Real-Time Sentiment Classification:** Evaluates raw movie reviews using pre-trained Hugging Face Transformer models and `scikit-learn` classification pipelines.
* **📊 Confidence & Rating Generation:** Calculates sentiment polarity scores and translates qualitative text reviews into quantitative rating metrics.
* **📈 Summary Analytics Dashboard:** Visualizes overall audience reception, sentiment distribution, and review insights through a clean web interface.
* **⚡ Decoupled Client-Server Architecture:** Separates the client-side interface (`Frontend`) from the Python inference engine (`Backend`) via RESTful API endpoints.
* **🧹 Automated Text Preprocessing:** Handles tokenization, stop-word removal, special character cleaning, and feature extraction prior to model inference.

---

## 📂 Repository Structure

```text
movie-review-ai/
├── .github/                # GitHub workflows and repository configuration
├── Backend/                # Python NLP engine, ML models, Flask/Streamlit server & API routes
├── Frontend/               # Interactive web UI built with HTML5, CSS3, and JavaScript
├── .gitignore              # Ignored virtual environments, cache, and build artifacts
└── README.md               # Project documentation
