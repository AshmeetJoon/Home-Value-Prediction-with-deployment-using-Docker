import os
import joblib  # Or 'pickle' if you saved it with that
import numpy as np
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
# Make sure the model file is in the same directory
model_path = "xgb_california_model.pkl"
model = joblib.load(model_path)

@app.route('/')
def home():
    return "XGBoost Model API is running."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json(force=True)
        
        # Extract the features (ensure this matches your model's input)
        # Assuming the input is a JSON object with a key "features"
        # that holds a list or list-of-lists.
        features = data['features']
        
        # Convert features to a numpy array for the model
        prediction_input = np.array(features)
        
        # Make a prediction
        prediction = model.predict(prediction_input)
        
        # Convert the prediction (often a numpy array) to a list
        output = prediction.tolist()
        
        # Return the prediction as JSON
        return jsonify(prediction=output)

    except Exception as e:
        # Return an error message if something goes wrong
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    # Get the port from the environment variable, default to 8000
    port = int(os.environ.get("PORT", 8000))
    # Run the app, accessible from any IP (0.0.0.0)
    app.run(host='0.0.0.0', port=port, debug=False)