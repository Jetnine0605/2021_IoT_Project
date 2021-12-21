import RPi.GPIO as GPIO

LED_PIN1 = 25
SWITCH_PIN1 = 12
LED_PIN2 = 16
SWITCH_PIN2 = 4
LED_PIN3 = 20
SWITCH_PIN3 = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1,GPIO.OUT)
GPIO.setup(SWITCH_PIN1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #내부풀다운저항
GPIO.setup(LED_PIN2,GPIO.OUT)
GPIO.setup(SWITCH_PIN2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #내부풀다운저항
GPIO.setup(LED_PIN3,GPIO.OUT)
GPIO.setup(SWITCH_PIN3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #내부풀다운저항

try:
    while True:
        val1 =GPIO.input(SWITCH_PIN1) #누르지 않은 경우 0, 눌렀을 떄는 1
        print(val1)
        GPIO.output(LED_PIN1,val1) #GPIO.HIGH (1),GPIO.LOW (0)
        val2 =GPIO.input(SWITCH_PIN2) #누르지 않은 경우 0, 눌렀을 떄는 1
        print(val2)
        GPIO.output(LED_PIN2,val2) #GPIO.HIGH (1),GPIO.LOW (0)
        val3 =GPIO.input(SWITCH_PIN3) #누르지 않은 경우 0, 눌렀을 떄는 1
        print(val3)
        GPIO.output(LED_PIN3,val3) #GPIO.HIGH (1),GPIO.LOW (0)
finally:
    GPIO.cleanup()
    print('cleanup and exit')

