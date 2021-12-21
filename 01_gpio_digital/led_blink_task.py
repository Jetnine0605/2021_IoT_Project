import RPi.GPIO as GPIO
import time

LED_PIN1 = 23
GPIO.setmode(GPIO.BCM)  #GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN1, GPIO.OUT)    #GPIO.OUT or GPIO.IN

LED_PIN2 = 24
GPIO.setup(LED_PIN2, GPIO.OUT)    #GPIO.OUT or GPIO.IN

LED_PIN3 = 25
GPIO.setup(LED_PIN3, GPIO.OUT)    #GPIO.OUT or GPIO.IN

for i in range(10):
    GPIO.output(LED_PIN1, GPIO.HIGH) # 1
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN1, GPIO.LOW) # 0
    print("led off")
    time.sleep(0)
    GPIO.output(LED_PIN2, GPIO.HIGH) # 1
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN2, GPIO.LOW) # 0
    print("led off")
    time.sleep(0)
    GPIO.output(LED_PIN3, GPIO.HIGH) # 1
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN3, GPIO.LOW) # 0
    print("led off")
    time.sleep(0)

GPIO.cleanup()  # GPIO 핀상태 초기화    
















