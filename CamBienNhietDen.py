import Adafruit_DHT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

sensor = Adafruit_DHT.DHT11

gpio = 4

while (True):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
    if temperature < 20 :
        GPIO.output(14,1)
        GPIO.output(15,0)
        GPIO.output(18,0)
    elif temperature >= 20 & temperature < 27:
        GPIO.output(14,0)
        GPIO.output(15,1)
        GPIO.output(18,0)
    else:
        GPIO.output(14,0)
        GPIO.output(15,0)
        GPIO.output(18,1)
