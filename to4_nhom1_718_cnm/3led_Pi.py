
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
# Set GPIO sensor is connected to
GREEN = 13
YELLOW = 19
RED = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
while True:
    GPIO.output(GREEN,GPIO.HIGH)
    time.sleep(5);
    GPIO.output(GREEN,GPIO.LOW) 
    GPIO.output(YELLOW,GPIO.HIGH)
    time.sleep(3);
    GPIO.output(YELLOW,GPIO.LOW)
    GPIO.output(RED,GPIO.HIGH)
    time.sleep(4);
    GPIO.output(RED,GPIO.LOW)







