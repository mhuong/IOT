import RPi.GPIO as GPIO
import time
 
def led(LED, time_sleep):
	GPIO.output(LED,GPIO.HIGH) # bật đèn led
	time.sleep(time_sleep) # thời gian hoạt động
	GPIO.output(LED,GPIO.LOW) # tắt đèn
 
KHIGA = 22
BUZZER = 25 # Khai báo chân buzz 12
LED_RED = 14 #Chân Led đỏ 8
LED_GREEN = 15 #Chan led xanh 10
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(KHIGA, GPIO.IN) # lấy tín hiệu từ PIR
GPIO.setup(BUZZER,GPIO.OUT) #kích hoạt buzzer
GPIO.setup(LED_RED,GPIO.OUT) #kích hoạt LED đỏ
GPIO.setup(LED_GREEN,GPIO.OUT) #kích hoạt GREEN đỏ

def buzz(BUZZER) :
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(BUZZER, GPIO.LOW)
    time.sleep(1)
         

try:
	while True:
		i=GPIO.input(22)
		if i>200:
			print("Khi ga >200")
			led(LED_RED, 2)
			buzz(BUZZER)
			# đèn led đỏ sáng, và còi hú báo động
		else:
			print("Khi ga <200")
			led(LED_GREEN, 2)
			buzz(BUZZER)
		time.sleep(3) # nghỉ 3s cho đến vòng lặp tiếp theo
	
except KeyboardInterrupt:
	print("Exception: KeyboardInterrupt")
 
finally:
	GPIO.cleanup() # dọn dẹp sau khi sử dụng