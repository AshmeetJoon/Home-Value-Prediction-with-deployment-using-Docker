
import requests
import json
import sys

# --- CONFIGURATION ---
# This is the address where your Docker container is running (accessible locally)
API_URL = "http://localhost:9999/predict"

# -----------------------------------------------------------------------------------------
# *** EDIT THIS LINE (The 8 numbers inside the brackets) TO PREDICT A NEW HOUSE PRICE ***
# Order: [ MedInc, HouseAge, Avg Rooms, Avg Bedrms, Population, Avg Occupancy, Latitude, Longitude ]
HOUSE_FEATURES = [ 8.3, 41.0, 6.9, 1.0, 322.0, 2.5, 37.8, -122.2 ] 
# -----------------------------------------------------------------------------------------

data_to_predict = {"features": [HOUSE_FEATURES]}

print("Attempting to connect to deployed ML model at:", API_URL)
try:
    # Send the data as JSON in a POST request
    response = requests.post(
        API_URL, 
        headers={"Content-Type": "application/json"},
        json=data_to_predict 
    )
    
    # Check for success (HTTP 200)
    if response.status_code == 200:
        result = response.json()
        predicted_value = result.get('prediction')[0]
        
        print("\n=============================================")
        print("✅ PREDICTION SUCCESSFUL")
        print("=============================================")
        print(f"Features Sent: {HOUSE_FEATURES}")
        # The model predicts the value in units of $100,000, so we convert it:
        print(f"Predicted Median House Value: ${predicted_value * 100000:.2f}")
        print("=============================================\n")
    else:
        # Handle API or data errors
        print(f"\n[ERROR] API Returned Status Code {response.status_code}")
        print(f"Server Response: {response.text}")

except requests.exceptions.ConnectionError:
    print("\n[CRITICAL ERROR] Failed to connect to localhost:9999.")
    print("Is the Docker container running? Check with 'docker ps'")
except Exception as e:
    print(f"\n[UNEXPECTED ERROR] {e}")

# This will remind you to install the library if needed
if 'requests' not in sys.modules:
    print("\n[NOTE] Remember to install required libraries with 'pip install requests'")