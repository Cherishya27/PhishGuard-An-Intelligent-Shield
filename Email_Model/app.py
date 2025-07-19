from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import re
from scipy.sparse import hstack

# Load model and vectorizer
model = joblib.load('xgb_phishing_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')
scaler = joblib.load('custom_scaler.pkl')

# Feature Engineering (same as training)
def extract_custom_features(text):
    feats = pd.DataFrame([{
        'num_links': len(re.findall(r'http[s]?://', text.lower())),
        'has_phishing_keywords': int(any(k in text.lower() for k in [
            'verify', 'account suspended', 'login now', 'reset password', 'gift card'])),
        'uses_non_https_links': int('http://' in text.lower() and 'https://' not in text.lower()),
        'suspicious_url_pattern': int(bool(re.search(r'\b(secure|login|update|account)[-_]?(info|center)?\b', text.lower()))),
        'greeting_generic': int('dear customer' in text.lower() or 'dear user' in text.lower())
    }])
    return scaler.transform(feats)

# Initialize Flask
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    email_text = data.get("email_text", "")

    if not email_text.strip():
        return jsonify({"error": "Email text is empty."}), 400

    try:
        tfidf_feat = vectorizer.transform([email_text])
        custom_feat = extract_custom_features(email_text)
        combined = hstack([tfidf_feat, custom_feat])
        prediction = model.predict(combined)[0]
        label = "Phishing Email" if prediction == 1 else "Safe Email"
        return jsonify({"prediction": int(prediction), "label": label})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
