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

# This allows running the script independently for testing
if __name__ == "__main__":
    # Set the GPIO pin
    GPIO_PIN = 17

    try:
        # Set up GPIO
        setup_gpio(GPIO_PIN)

        while True:
            # Measure distance
            distance = measure_distance(GPIO_PIN)
            print(f"Distance: {distance} cm")
            time.sleep(1)

    except KeyboardInterrupt:
        # Clean up GPIO on keyboard interrupt
        GPIO.cleanup()
