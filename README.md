# 🧠 AI Spam Analyzer Pro

A machine learning-powered web application that detects whether a message is **Spam or Not Spam** using advanced NLP techniques and ensemble learning.

---

## 🚀 Live Demo

👉 *(Add your Render link here after deployment)*
Example: https://your-app.onrender.com

---

## 📌 Features

* 🔍 Spam Detection using Machine Learning
* 🧠 TF-IDF Vectorization with n-grams
* 🤖 Multiple Models:

  * Naive Bayes
  * Support Vector Machine (SVM)
  * Random Forest
* ⚡ Ensemble Learning (Voting System)
* 📊 Confidence Score & Risk Level
* 🧾 Important Words Extraction
* 📈 Model Comparison View
* 🕘 Recent History Tracking
* 🎨 Clean & Interactive UI

---

## 🧠 How It Works

1. User enters a message
2. Text is preprocessed (cleaned & normalized)
3. TF-IDF converts text → numerical features
4. Multiple ML models make predictions
5. Ensemble voting decides final result
6. Confidence score and insights are displayed

---

## 🛠 Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Flask (Python)
* **Machine Learning:** scikit-learn
* **Deployment:** Render

---

## 📂 Project Structure

```
ai-spam-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── nb_model.pkl
├── svm_model.pkl
├── rf_model.pkl
├── vectorizer.pkl
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-spam-analyzer.git
cd ai-spam-analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Application

```bash
python app.py
```

### 4. Open in Browser

```
http://127.0.0.1:10000
```

---

## 📊 Model Details

* **Vectorization:** TF-IDF (with n-grams)
* **Algorithms Used:**

  * Multinomial Naive Bayes
  * Linear SVM
  * Random Forest
* **Accuracy:** ~97–98%
* **Improvement Techniques:**

  * Text preprocessing
  * Dataset augmentation
  * Ensemble learning

---

## 🧠 Key Learning Outcomes

* Natural Language Processing (NLP)
* Feature Engineering (TF-IDF)
* Ensemble Machine Learning
* Model Evaluation & Optimization
* Full-stack ML Deployment

---

## 🔮 Future Improvements

* 📂 Bulk message (CSV) analysis
* 🔐 User authentication system
* 📊 Advanced analytics dashboard
* 📧 Gmail/Email integration
* 🌐 REST API support

---

## 👨‍💻 Author

**Sai Teja Goshika**
📧 [goshikasaiteja137@gmail.com](mailto:goshikasaiteja137@gmail.com)

---

Deployed link : https://ai-spam-analyzer.onrender.com/

## ⭐ If you like this project

Give it a ⭐ on GitHub!
