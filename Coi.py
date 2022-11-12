import RPi.GPIO as GPIO
import time

try:
    input = raw_input
except NameError:
    pass

buzzer_pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer_pin, GPIO.OUT)

def buzz(pitch, duration) :
    period = 1.0 / pitch
    half_period = period / 2
    cycles = int(duration * pitch)
    for i in range(cycles) :
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(half_period )
        GPIO.output(buzzer_pin, GPIO.LOW)
        time.sleep(half_period )

try:
    while True :
        buzz(210, 220)

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    GPIO.cleanup()          
