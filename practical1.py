import RPi.GPIO as GPIO
from time import sleep

# Set the pin numbering scheme to the physical board layout
GPIO.setmode(GPIO.BOARD)

# Set pin 12 as an output pin
# Note: You should replace '12' with the actual physical pin number you are using
GPIO.setup(12, GPIO.OUT)

try:
    # Start an infinite loop
    while True:
        # Turn the output 'on' (High)
        GPIO.output(12, GPIO.HIGH)
        # Wait for 1 second
        sleep(1)

        # Turn the output 'off' (Low)
        GPIO.output(12, GPIO.LOW)
        # Wait for 1 second
        sleep(1)

# This block ensures the GPIO pins are cleaned up when you stop the script
except KeyboardInterrupt:
    GPIO.cleanup()