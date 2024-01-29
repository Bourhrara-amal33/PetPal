import requests
import json
import time

def send_data_to_firebase(distance):
    url = "https://petpal-petfeeder-default-rtdb.europe-west1.firebasedatabase.app/ultrasound_distance.json"

    payload = {
        "distance": distance,
        "date": time.strftime("%x"),
        "time": time.strftime("%X"),
        "device": "ultrasound-sensor"
    }

    headers = {
        "Content-Type": "application/json"
    }

    # Assuming you want to perform a POST request, change to "PUT" if needed
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    print(response.text)

# This allows running the script independently for testing
if __name__ == "__main__":
    # Example usage
    distance_value = 42.0  # Replace with the actual distance value
    send_data_to_firebase(distance_value)
