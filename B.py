import RPi.GPIO as GPIO
import Adafruit_DHT #library of sensor DHT
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
RED_LED_PIN = 17 #GPIO = 11 BOARD
GREEN_LED_PIN = 27 #GPIO = 13 BOARD
YELLOW_LED_PIN = 22 #GPIO = 15 BOARD
DHT_PIN = 4 #GPIO = 7 BOARD
BUZZER_PIN = 14 #GPIO = 8 BOARD
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_LED_PIN, GPIO.OUT)

DHT_SENSOR = Adafruit_DHT.DHT11
while True:
    time.sleep(1)
    humidity,temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity == None and temperature == None:
        continue
    if (temperature<20):
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
        GPIO.output(YELLOW_LED_PIN, GPIO.LOW)
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        print("Temp={0:0.1f}C  Humidity={1:0.1f}%  =>> RED turn on".format(temperature, humidity))
    elif (temperature >20) and (temperature <=25):
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        GPIO.output(YELLOW_LED_PIN, GPIO.HIGH)
        print("Temp={0:0.1f}C  Humidity={1:0.1f}%  =>> YELLOW turn on".format(temperature, humidity))
    else :
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        GPIO.output(YELLOW_LED_PIN, GPIO.LOW)
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)
        print("Temp={0:0.1f}C  Humidity={1:0.1f}%  =>> GREEN turn on".format(temperature, humidity))
