from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

@app.route('/')
def home():
    return render_template('index.html')  # Loads the UI page

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form['message']  # Get message from form input
    transformed_data = vectorizer.transform([data])  # Convert text to numerical
    prediction = model.predict(transformed_data)  # Predict spam or not spam

    result = "spam" if prediction[0] == 1 else "ham"
    
    # Return JSON instead of reloading HTML
    return jsonify({'prediction': result})  

if __name__ == '__main__':
    app.run(debug=True)
