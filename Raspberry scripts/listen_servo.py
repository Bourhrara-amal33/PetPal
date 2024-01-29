import RPi.GPIO as GPIO
import requests
import time

# Set the GPIO pin for the servo
SERVO_PIN = 18

# Set up the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Create a PWM object with a frequency of 50Hz
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(2.5)  # Initial position

# Firebase Realtime Database URL and endpoint
firebase_url = "https://petpal-petfeeder-default-rtdb.europe-west1.firebasedatabase.app"
servo_data_endpoint = "/servoMotorData.json"

# Function to fetch servo data from Firebase and delete the entry
def fetch_and_delete_servo_data():
    try:
        # Make a GET request to the Firebase endpoint
        response = requests.get(firebase_url + servo_data_endpoint)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            servo_data = response.json()

            # Delete the data from Firebase
            requests.delete(firebase_url + servo_data_endpoint)

            return servo_data
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
            return None

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Function to control the servo based on servo data
def control_servo_based_on_data(data):
    try:
        # Iterate through the entries in the response
        for key, servo_entry in data.items():
            left_value = servo_entry.get('left', False)
            right_value = servo_entry.get('right', False)

            # Assuming you want to control the servo based on Left and Right values
            if left_value:
                pwm.ChangeDutyCycle(7.5)
                print("left")
            elif right_value:
                pwm.ChangeDutyCycle(2.5)
                print("right")
            else:
                # Stop the servo
                pwm.ChangeDutyCycle(0)

            return True

    except Exception as e:
        print(f"Error: {str(e)}")
        return False

# Continuous loop to fetch and control servo data
try:
    while True:
        # Fetch and delete servo data from Firebase
        servo_data = fetch_and_delete_servo_data()

        if servo_data:
            # Control the servo based on fetched data
            result = control_servo_based_on_data(servo_data)

            if result:
                print("Servo controlled successfully.")
            else:
                print("Failed to control servo.")

        else:
            print("Failed to fetch servo data.")

        # Sleep for a specific duration before fetching data again
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO
    pwm.stop()
    GPIO.cleanup()
