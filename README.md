# SMS Spam Detection - AI Application

## Overview
This project is an AI-based SMS Spam Detection application that classifies messages as **Spam** or **Not Spam** using a Machine Learning model. The project includes data preprocessing, model training, deployment of an API using Flask, and hosting on **Render** for live access.

## Features
- **Preprocessing**: Text data cleaning and feature extraction
- **Model Training**: Traditional ML model (Logistic Regression)
- **Web API**: Flask-based API for spam detection
- **User Interface**: Simple and interactive UI for message classification
- **Deployment**: Hosted on **Render** for online accessibility

---
## 1️⃣ Data Preparation & Model Training

### Steps Performed:
1. **Dataset Used**: SMS Spam Collection Dataset
2. **Preprocessing**: Removed stopwords, tokenized text, converted text to vectors using TF-IDF.
3. **Model Training**:
   - Used **Logistic Regression** for classification.
   - Split dataset into training & testing.
   - Achieved good accuracy with optimized hyperparameters.
4. **Saving the Model**:
   - Saved trained **model** as `spam_model.pkl`.
   - Saved **TF-IDF Vectorizer** as `tfidf_vectorizer.pkl`.

---
## 2️⃣ Creating API using Flask

### Steps Performed:
1. **Created a Flask Application** (`app.py`)
   - Loads the model and vectorizer.
   - Accepts input from users.
   - Predicts whether a message is **Spam** or **Not Spam**.
2. **Tested API using Postman**.
   - Screenshot of **Postman API Testing**:
     ![Postman API Test](https://github.com/Kritika-saha/Projects-advance-analytics/blob/main/screenshots/Screenshot%202025-03-30%20193536.png)

---
## 3️⃣ Frontend - Web Interface

### Steps Performed:
1. **Created `index.html`**
   - User-friendly **form to input messages**.
   - Displays output **in color-coded format** (Spam - Red, Not Spam - Green).
2. **Updated `app.py`**
   - Added `render_template` for displaying results dynamically.

---
## 4️⃣ Deployment on Render

### Steps Performed:
1. **Pushed code to GitHub**
   - Used `git add .`, `git commit -m "Initial commit"`, `git push origin main`
2. **Created a Render Web Service**
   - Connected GitHub repo to Render.
   - It will create a workspace and the dashboard will look like this:
     ![Dashboard](https://github.com/Kritika-saha/Projects-advance-analytics/blob/main/screenshots/Screenshot%202025-03-30%20222455.png)
   - If we click on webs services we can select the directory where our files are present and click on Deploy.
   - It will deploy and build the API successfully.
3. **Tested API on Render using Postman**
   - Screenshot of **Render API Test in Postman**:
     ![Render API Test](https://github.com/Kritika-saha/Projects-advance-analytics/blob/main/screenshots/Screenshot%202025-03-31%20103114.png)

### Deployed API Link:
[https://projects-advance-analytics.onrender.com](https://projects-advance-analytics.onrender.com)
-Application:
![Application](https://github.com/Kritika-saha/Projects-advance-analytics/blob/main/screenshots/Screenshot%202025-04-02%20211236.png)

---
## 5️⃣ How to Run Locally

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/Kritika-saha/Projects-advance-analytics.git
   cd Projects-advance-analytics
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Flask App:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000/` in your browser.

---
## 6️⃣ Future Enhancements
- Improve UI with better styling.
- Implement additional ML models for better accuracy.
- Add database storage for spam message tracking.


---
🎯 This project was built as part of an AI-based application development activity. 🚀

