# PhishGuard-An-Intelligent-Shield
Two ML classifiers to detect phishing emails and malicious websites. Engineered features such as URL entropy, phishing keyword presence, non-HTTPS usage, and generic greeting detection. Trained models using XGBoost, Logistic Regression, and TF-IDF vectorization. Deployed in a Flask-based web app.

The MLmodel was developed for Phishing Detection of Emails, it analyzes the content of an email to decide whether it is a phishing attempt or a legitimate message. It reads the text of the email and checks for suspicious links, urgent language, generic greetings, and phishing-related keywords. By combining text analysis (NLP) and intelligent pattern detection, it can accurately classify emails and help protect users from scams.

The ML model of Phishing Detection of Websites checks if a given website URL is genuine or malicious. It analyzes features like how the URL is structured, how long and complex it is, and especially a unique feature called URL entropy, which helps detect fake or randomly generated domains often used in phishing. Based on this, the model predicts whether the website is safe to visit or potentially harmful.

Abstract:
In today’s digital landscape, phishing attacks pose a significant threat to individuals and organizations by exploiting trust through deceptive emails and websites. This project addresses the issue by developing two intelligent machine learning models to detect phishing attempts with high accuracy.
The first model focuses on identifying phishing emails by analyzing the textual content using Natural Language Processing (NLP). It incorporates both traditional techniques like TF-IDF and a set of handcrafted features — including the number of hyperlinks, phishing-related keywords, non-secure links, suspicious URL patterns, and generic greeting styles. This hybrid approach allows the model to capture both linguistic cues and behavioral patterns typical of phishing attempts.
The second model targets phishing websites by evaluating URLs and structured data. Alongside over 80 technical features from the dataset, the model introduces a novel attribute — URLentropy, which measures the randomness and complexity of characters in a URL. Phishing websites often use obfuscated and irregular links, and entropy provides a mathematical measure to flag such anomalies.
Both models are trained using robust classifiers like XGBoost and Logistic Regression, and evaluated on real-world datasets. To enhance usability, the models are integrated into separate Flask web applications with interactive frontends that not only predict threats but also explain the underlying decision using visible feature insights.
This dual-model system provides a reliable and user-friendly solution for detecting phishing threats in real-time, contributing to the broader goal of cybersecurity awareness and defense.

METHODOLOGY

Modules

Email Feature Extractor: Extracts useful information from email text such as number of hyperlinks, presence of phishing related words, whether it uses non-secure links, suspicious sentence patterns, and the greeting style (generic vs personalized). These features help the model understand the nature of the message.

URL Feature Extractor: Processes website URLstoderivemeaningfulfeatures. These include character-based metrics, domain related info, and a custom metric called URL entropy that measures randomness — often high in phishing links. This module prepares input for the model.

Classification Engine: The heart of the system. This module loads the trained machine learning models (for emails and URLs) and makes predictions:
 • 1→Phishing
 • 0→Legitimate
 It combines extracted features with the models to make accurate predictions.
 
Frontend Display(HTML, CSS, JS): This is the user interface that allows users to input an email or URL, submit it, and view the prediction. It also shows feature-based reasoning, helping users understand why the model flagged it as phishing or safe.

Data Collection

Phishing Email Dataset from Kaggle Used to train the email model. It contains real-world phishing and legitimate email texts, allowing the model to learn from various writing styles and scam patterns.

Phishing Website Dataset Collected the dataset from kaggle https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset It accomodates both phishing and legitimate URL’s. Trained the model using this large dataset.

URL’s Labeled as Phishing/Legitimate All collected URLs are labeled (manually or via trusted sources) to help the model learn how phishing links differ from safe ones.

Emails labeled manually or via trusted public corpora Email samples are labeled as phishing or safe based on manual inspection or from Kaggle datasets. This ensures a balanced dataset for training.

Preprocessing

Emails
 Before feeding email text into the model, we clean and prepare it:
 • Remove HTMLtags (if any)
 • Convert all text to lowercase
 • Tokenize (split into words)
 • Remove stopwords (like ”the”, ”is”, ”and”)

URLS
 URLs are also cleaned and converted into numerical features. We extract:
 • Path segments
 • Presence of symbols like “-”, “@”, or “.”
 • Count of special characters or digits
 • URLEntropy —akey feature that helps detect obfuscation (e.g., random-looking URLs)
 4.4. Feature Engineering
 4.4.1. Email Model Features
 • Numberof Links: Counts how many hyperlinks (http://, https://) exist in the email.
 • Presence of Phishing Keywords: Detects words like ”verify”, ”account locked”, ”urgent”,
 etc.
 • Generic Greetings: Flags if the message starts with ”Dear user”, ”Dear customer”, etc.
 • Suspicious Patterns: Checks for misleading phrases or suspicious URL formatting.
 
 URL Model Features
 Structured Features- 80+ attributes from phishing dataset, such as:
 • URLlength
 • Number of dots, hyphens
 • HTTPSpresence
 • Domain age and popularity
 Custom Feature– URL Entropy:
 • Measures randomness in a URL
 • Higher entropy usually means a phishing link
 • Unique addition not commonly found in standard models

IMPLEMENTATIONDETAILS

Technology Stack

The project was developed using a combination of backend, machine learning, and frontend technologies:
 • Python: Core programming language used for model development, feature engineering, and
 backend logic.
 • Flask: Lightweight Python web framework used to serve the models and handle API requests.
 • Scikit-learn: Used for preprocessing, training traditional ML models like Logistic Regression.
 • XGBoost: High-performance gradient boosting library used for the final phishing detection
 models (for both email and URLs).
 • Pandas: Used for data cleaning, manipulation, and feature extraction.
 • HTML,CSS,JavaScript: Technologies used to build the user interface. These allow users to
 interact with the model through a clean web page.

System Architecture
 The architecture follows a modular and REST-based structure. Two separate models were created,
 One for email phishing detection and other for URL-based phishing detection. Each model is served
 via individual Flask APIs. The frontend sends user input (email text or URL) to the appropriate
 backend endpoint. Backend processes the input, applies preprocessing and feature extraction, makes
 the prediction, and sends back the result in JSON format. This separation ensures modularity, so each
 model can be maintained and improved independently.

User Interface
 The UI was designed with simplicity and usability in mind. Users are provided with a text input area
 to paste email content or enter a URL. A predict button submits the input to the backend and shows
 the result (safe or phishing). The interface also displays a breakdown of features used in the prediction
 like, Number of links, Keyword detection, Suspicious URL patterns and URL entropy. This increases
 transparency and helps users understand why a particular result was shown.

Integration
 The entire system is integrated using Flask. Each model (email URL) was trained separately and
 saved as .pkl files using joblib. The Flask server loads these models and handles predictions on
 demand. The frontend communicates with the backend using AJAX (JSON-based) requests. For
 each input, the backend returns, the Prediction result (Safe or Phishing), Feature-level insights. These
 results are shown in the UI dynamically, without refreshing the page. This architecture supports
 real-time, interactive phishing detection.

Security
 Basic but essential security measures are implemented. Input validation is performed on both frontend
 and backend to avoid crashes or misuse. The system does not store or log any user input, ensuring
 user privacy. All models run locally, so no data is sent to external servers. While not enterprise-level,
 these measures are enough for academic and prototype-level deployment.

Testing and Deployment
 Both models were tested using real-world phishing and legitimate data samples. The predictions were
 compared to actual labels using accuracy, F1-score, and ROC curves. The final models were saved
 using joblib for quick loading and inference. The Flask app and UI were runlocally on localhost:5000,
 but they can be deployed to services like, Heroku, Render and Railway. Testing confirmed that:
 • The email model works well with varied email formats.
 • The URL model performs accurately even with unfamiliar domain names due to entropy detection.

Results
 precision    recall  f1-score   support

           0       0.99      0.95      0.97      2265
           1       0.92      0.98      0.95      1464

    accuracy                           0.96      3729
   macro avg       0.96      0.96      0.96      3729
weighted avg       0.96      0.96      0.96      3729
