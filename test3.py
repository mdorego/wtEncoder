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
        print(enc_1.read())
        time.sleep(3)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Clean up GPIO on program exit
    GPIO.cleanup()
