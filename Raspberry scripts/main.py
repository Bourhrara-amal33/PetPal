import time
import sys
import json
import requests

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


import RPi.GPIO as GPIO
import time

def setup_gpio(gpio_pin):
    # Set up the GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_pin, GPIO.IN)

def measure_distance(gpio_pin):
        # Set the GPIO pin as output
    GPIO.setup(gpio_pin, GPIO.OUT)

    # Set the pin low for a short time to ensure a clean pulse
    GPIO.output(gpio_pin, GPIO.LOW)
    time.sleep(0.01)
    GPIO.output(gpio_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(gpio_pin, GPIO.LOW)

    # Set the GPIO pin as input
    GPIO.setup(gpio_pin, GPIO.IN)

    # Measure the time for the echo pulse
    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(gpio_pin) == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input(gpio_pin) == GPIO.HIGH:
        pulse_end = time.time()

    # Calculate the distance using the speed of sound (343 meters per second)
    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * 34300) / 2  # Distance in centimeters

    return distance
# Set the GPIO pin
GPIO_PIN = 17  # Change this to the actual GPIO pin you've connected to
DISTANCE_COUNT = 5  # Number of distances to collect

def collect_distances(gpio_pin, count):
    distances = []
    for _ in range(count):
        distance = measure_distance(gpio_pin)
        distances.append(distance)
        time.sleep(1)
    return distances

def calculate_mean(distances):
    return sum(distances) / len(distances) if distances else 0

try:
    # Set up GPIO
    setup_gpio(GPIO_PIN)

    # Collect 10 distances
    distances = collect_distances(GPIO_PIN, DISTANCE_COUNT)

    # Calculate the mean
    mean_distance = calculate_mean(distances)

    # Print the mean distance
    print(f"Mean Distance: {mean_distance:.2f} cm")

    # Send data to Firebase
    send_data_to_firebase(round(mean_distance,2))

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()

finally:
    # Exit the script after sending data to Firebase
    sys.exit()
