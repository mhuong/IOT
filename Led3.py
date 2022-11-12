import RPi.GPIO as GPIO
import time

LED_PIN1=14
LED_PIN2=15
LED_PIN3=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1,GPIO.OUT)
GPIO.setup(LED_PIN2,GPIO.OUT)
GPIO.setup(LED_PIN3,GPIO.OUT)

while True:
  GPIO.output(LED_PIN1,GPIO.HIGH)
  time.sleep(1)
  GPIO.output(LED_PIN1,GPIO.LOW)
  
  GPIO.output(LED_PIN2,GPIO.HIGH)
  time.sleep(1)
  GPIO.output(LED_PIN2,GPIO.LOW)
  
  GPIO.output(LED_PIN3,GPIO.HIGH)
  time.sleep(1)
  GPIO.output(LED_PIN3,GPIO.LOW)
  #time.sleep(2)

GPIO.cleanup()
