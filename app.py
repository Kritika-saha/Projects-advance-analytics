import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

# Load the saved model and vectorizer
with open("spam_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "SMS Spam Detection API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON input
        data = request.get_json()

        # Extract message text
        sms_text = data.get("message", "")

        # Transform using vectorizer
        transformed_text = vectorizer.transform([sms_text])

        # Make prediction
        prediction = model.predict(transformed_text)

        # Convert result
        result = "Spam" if prediction[0] == 1 else "Not Spam"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
