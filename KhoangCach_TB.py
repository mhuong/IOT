# Import required Python libraries
from __future__ import print_function
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)


# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24
LED=4

# Speed of sound in cm/s at temperature
temperature = 20
speedSound = 33100 + (0.6*temperature)

print("Ultrasonic Measurement")
print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
solan=1
sum=0
while (solan <=10):   #kiểm tra 5 lần
	# Set trigger to False (Low)
	GPIO.output(GPIO_TRIGGER, False)
	# Allow module to settle
	time.sleep(0.5)
	# Send 10us pulse to trigger
	GPIO.output(GPIO_TRIGGER, True)
	# Wait 10us
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	start = time.time()
	while GPIO.input(GPIO_ECHO)==0:
		start = time.time()
	while GPIO.input(GPIO_ECHO)==1:
		stop = time.time()
	# Calculate pulse length
	elapsed = stop-start
	# Distance pulse travelled in that time is time
	# multiplied by the speed of sound (cm/s)
	distance = elapsed * speedSound
	# That was the distance there and back so halve the value
	distance = distance / 2
	print("Khoảng cách đo lần ",solan," : {0:5.1f}".format(distance))
	sum=sum + distance
	solan =solan + 1
	time.sleep(0.5)
khoangcach = sum / 10
print("Distance trung bình: {0:5.4f}".format(khoangcach))
#print("Distance trung bình : {0:5.1f}".format(distance))
# Reset GPIO settings
GPIO.cleanup()
