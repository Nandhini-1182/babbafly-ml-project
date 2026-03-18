import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# model load
model = pickle.load(open("models/price_model.pkl", "rb"))

@app.route("/")
def home():
    return "API Running Successfully"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        brand = data["brand"]
        category = data["category"]
        rating = data["rating"]

        features = np.array([[brand, category, rating]])

        prediction = model.predict(features)

        return jsonify({
            "predicted_price":
            round(float(prediction[0]),2)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)