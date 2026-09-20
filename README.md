# FAQ Chatbot

A beginner-friendly FAQ chatbot built for CodeAlpha AI Internship Task 2.

## Features

- Simple chatbot user interface
- College FAQ dataset stored in JSON
- Text preprocessing using NLTK Porter Stemmer
- TF-IDF vectorization
- Cosine similarity for question matching
- Fallback response for unrelated questions
- Flask web application
- Render-ready deployment
- Health-check endpoint

## Technologies

- Python
- Flask
- NLTK
- Scikit-learn
- HTML
- CSS
- Gunicorn

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000/
```

Health check:

```text
http://127.0.0.1:5000/health
```

## Render

Build command:

```text
pip install -r requirements.txt
```

Start command:

```text
gunicorn app:app
```

## CodeAlpha

This project is created for Task 2: Chatbot for FAQs.
