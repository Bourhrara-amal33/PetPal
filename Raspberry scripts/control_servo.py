import RPi.GPIO as GPIO
import time

# Set the GPIO pin for the servo
SERVO_PIN = 18

# Set up the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Create a PWM object with a frequency of 50Hz
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(2.5)  # Initial position

try:
    while True:
        # Move the servo to one position
        pwm.ChangeDutyCycle(7.5)
        time.sleep(1)

        # Move the servo to the other position
        pwm.ChangeDutyCycle(2.5)
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
