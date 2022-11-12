import RPi.GPIO as GPIO
import time
 
def led(LED, time_sleep):
	GPIO.output(LED,GPIO.HIGH) # bật đèn led
	time.sleep(time_sleep) # thời gian hoạt động
	GPIO.output(LED,GPIO.LOW) # tắt đèn
 
PIR = 7
BUZZER = 12 # Khai báo chân buzz 12
LED_RED = 8 #Chân Led đỏ 8
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR, GPIO.IN) # lấy tín hiệu từ PIR
GPIO.setup(BUZZER,GPIO.OUT) #kích hoạt buzzer
GPIO.setup(LED_RED,GPIO.OUT) #kích hoạt LED đỏ

def buzz(BUZZER) :
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(BUZZER, GPIO.LOW)
    time.sleep(3) 

try:
	while True:
		i=GPIO.input(7)
		if i==1: # Nếu phát hiện vật thể
			print("Phat hien vat the")
			led(LED_RED, 3)
			buzz(BUZZER)
			# đèn led đỏ sáng, và còi hú báo động trong 3s
		elif i==0: # Nếu không phát hiện vật thể
			print("Khong phat hien vat the")
		
		time.sleep(3) # nghỉ 3s cho đến vòng lặp tiếp theo
	
except KeyboardInterrupt:
	print("Exception: KeyboardInterrupt")
 
finally:
	GPIO.cleanup() # dọn dẹp sau khi sử dụng
