from flask import Flask, render_template, request
import json
import re

from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

stemmer = PorterStemmer()

with open("faq_data.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)


def preprocess(text):
    """Clean and stem text for NLP matching."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    words = text.split()
    words = [stemmer.stem(word) for word in words]
    return " ".join(words)


questions = [preprocess(item["question"]) for item in faqs]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(questions)


def find_answer(user_question):
    cleaned_question = preprocess(user_question)

    if not cleaned_question.strip():
        return "Please enter a question.", 0.0

    user_vector = vectorizer.transform([cleaned_question])
    similarities = cosine_similarity(user_vector, faq_vectors)[0]

    best_index = similarities.argmax()
    best_score = float(similarities[best_index])

    # Avoid returning an unrelated FAQ.
    if best_score < 0.15:
        return (
            "Sorry, I could not find a good answer to your question. "
            "Please try asking about admissions, courses, fees, timings, "
            "library, exams, hostel, or contact details."
        ), best_score

    return faqs[best_index]["answer"], best_score


@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    question = ""

    if request.method == "POST":
        question = request.form.get("question", "").strip()
        answer, _ = find_answer(question)

    return render_template(
        "index.html",
        question=question,
        answer=answer
    )


@app.route("/health")
def health():
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
