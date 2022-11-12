import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)#xanh
GPIO.setup(15, GPIO.OUT)#vang
GPIO.setup(18, GPIO.OUT)#do

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    humidity, temp = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temp is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temp, humidity))
        if temp > 25:
            GPIO.output(14,False)
            GPIO.output(15,False)
            GPIO.output(18,True)
            time.sleep(1)
        elif temp < 20:
            GPIO.output(14,True)
            GPIO.output(15,False)
            GPIO.output(18,False)
            time.sleep(1)
        else:
            GPIO.output(14,False)
            GPIO.output(15,True)
            GPIO.output(18,False)
            time.sleep(1)
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(3);
    
