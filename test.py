import Encoder

ENCODER1_PIN_A = 16
ENCODER1_PIN_B = 18
ENCODER2_PIN_A = 28
ENCODER2_PIN_B = 26
BUTTON_PIN_1 = 22
BUTTON_PIN_2 = 24

enc_1 = Encoder.Encoder(ENCODER1_PIN_A, ENCODER1_PIN_B)
enc_2 = Encoder.Encoder(ENCODER2_PIN_A, ENCODER2_PIN_B)

print(enc_1.read())
print(enc_2.read())
