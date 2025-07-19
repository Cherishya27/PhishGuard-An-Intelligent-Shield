from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import re
import math
from collections import Counter
from sklearn.preprocessing import StandardScaler
from scipy.sparse import hstack

# Load model, scaler, and features
model = joblib.load('xgb_web_model.pkl')
scaler = joblib.load('web_scaler.pkl')
features = joblib.load('web_features.pkl')

# Function to calculate URL entropy
def calculate_entropy(url):
    prob = [v / len(url) for v in Counter(url).values()]
    return -sum(p * math.log2(p) for p in prob) if len(url) > 0 else 0

# Initialize Flask
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get("url", "")
    
    if not url.strip():
        return jsonify({"error": "URL is empty."}), 400

    try:
        entropy = calculate_entropy(url)
        input_df = pd.DataFrame([[0]*len(features)], columns=features)
        input_df['url_entropy'] = entropy
        input_scaled = scaler.transform(input_df)

        prediction = model.predict(input_scaled)[0]
        label = "Phishing Website" if prediction == 1 else "Legitimate Website"

        return jsonify({
            "prediction": int(prediction),
            "label": label,
            "url_entropy": round(entropy, 4)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
