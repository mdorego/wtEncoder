import RPi.GPIO as GPIO
import time
import Encoder

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the rotary encoders
ENCODER1_PIN_A = 16
ENCODER1_PIN_B = 18
ENCODER2_PIN_A = 28
ENCODER2_PIN_B = 26

enc_1 = Encoder.Encoder(ENCODER1_PIN_A, ENCODER1_PIN_B)
enc_2 = Encoder.Encoder(ENCODER2_PIN_A, ENCODER2_PIN_B)

enc_1_prev = enc_1.read()
enc_2_prev = enc_2.read()

try:
    while True:
        current_value_1 = enc_1.read()
        current_value_2 = enc_2.read()

        if current_value_1 != enc_1_prev:
            if current_value_1 > enc_1_prev:
                print("Encoder 1 turned clockwise")
            else:
                print("Encoder 1 turned counterclockwise")
            enc_1_prev = current_value_1

        if current_value_2 != enc_2_prev:
            if current_value_2 > enc_2_prev:
                print("Encoder 2 turned clockwise")
            else:
                print("Encoder 2 turned counterclockwise")
            enc_2_prev = current_value_2

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Clean up GPIO on program exit
    GPIO.cleanup()
