from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("salary_prediction_model.pkl")

@app.route("/")
def home():
    return "Salary Prediction API is running!"

# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    # Convert input data into DataFrame
    df = pd.DataFrame([data])
    
    prediction = model.predict(df)
    
    return jsonify({
        "predicted_salary": float(prediction[0])
    })

# Run server
if __name__ == "__main__":
    app.run(debug=True)