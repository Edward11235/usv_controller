import Jetson.GPIO as GPIO
import time

# Pin Definitions
input_pin = 7  # Adapt this pin number to match the Jetson's GPIO pin you're using

# Pin Setup
GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
GPIO.setup(input_pin, GPIO.IN)  # set pin as an input pin

try:
    while True:
        if GPIO.input(input_pin):
            print("Input pin is HIGH")
        else:
            print("Input pin is LOW")
        time.sleep(0.1)
finally:
    GPIO.cleanup()
