from flask import Flask, request, render_template
import pickle
import os
import re

app = Flask(__name__)

# Load models
nb_model = pickle.load(open("nb_model.pkl","rb"))
svm_model = pickle.load(open("svm_model.pkl","rb"))
rf_model = pickle.load(open("rf_model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

history = []

# Text cleaning (same as training)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

@app.route('/')
def home():
    return render_template(
        "index.html",
        prediction_text=None,
        confidence=0,
        color="white",
        history=[],
        model_results={},
        risk="LOW",
        important_words=[]
    )

@app.route('/predict', methods=['POST'])
def predict():
    global history

    message = request.form['message']
    clean_msg = clean_text(message)

    data = vectorizer.transform([clean_msg])

    # Predictions
    nb_pred = nb_model.predict(data)[0]
    svm_pred = svm_model.predict(data)[0]
    rf_pred = rf_model.predict(data)[0]

    # Ensemble decision
    final = round((nb_pred + svm_pred + rf_pred)/3)

    label = "🚨 Spam" if final == 1 else "✅ Not Spam"
    color = "#ff4d4d" if final == 1 else "#00ffcc"

    # Weighted confidence
    confidence = round((0.2*nb_pred + 0.4*svm_pred + 0.4*rf_pred) * 100, 2)

    # Risk level
    if confidence > 70:
        risk = "HIGH"
    elif confidence > 30:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    # Model comparison
    model_results = {
        "Naive Bayes": "Spam" if nb_pred else "Not Spam",
        "SVM": "Spam" if svm_pred else "Not Spam",
        "Random Forest": "Spam" if rf_pred else "Not Spam"
    }

    # Important words (top TF-IDF features)
    feature_names = vectorizer.get_feature_names_out()
    vector_data = data.toarray()[0]

    important_words = []
    for i in range(len(vector_data)):
        if vector_data[i] > 0:
            important_words.append(feature_names[i])

    important_words = important_words[:6]

    # History
    history.insert(0, f"{message[:40]} → {label}")
    history = history[:5]

    return render_template(
        "index.html",
        prediction_text=label,
        color=color,
        confidence=confidence,
        model_results=model_results,
        history=history,
        risk=risk,
        important_words=important_words
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)