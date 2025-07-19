# PhishGuard-An-Intelligent-Shield
Two ML classifiers to detect phishing emails and malicious websites. Engineered features such as URL entropy, phishing keyword presence, non-HTTPS usage, and generic greeting detection. Trained models using XGBoost, Logistic Regression, and TF-IDF vectorization. Deployed in a Flask-based web app.

The MLmodel was developed for Phishing Detection of Emails, it analyzes the con
tent of an email to decide whether it is a phishing attempt or a legitimate message. It
 reads the text of the email and checks for suspicious links, urgent language, generic
 greetings, and phishing-related keywords. By combining text analysis (NLP) and intel
ligent pattern detection, it can accurately classify emails and help protect users from
scams.
 The ML model of Phishing Detection of Websites checks if a given website URL is
 genuine or malicious. It analyzes features like how the URL is structured, how long and
 complex it is, and especially a unique feature called URL entropy, which helps detect
 fake or randomly generated domains often used in phishing. Based on this, the model
 predicts whether the website is safe to visit or potentially harmful
