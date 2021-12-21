import RPi.GPIO as GPIO
import time
#필요한 것들 임포트해주기

PIR_PIN = 15
LED_PIN = 14
BUZZER_PIN = 13

SEGMENT_PINS1 = [2, 3, 4, 5, 6, 7]
SEGMENT_PINS2 = [8, 9, 10, 11, 12]

# 핀 번호 설정하기
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(PIR_PIN, GPIO.IN, GPIO.PUD_UP)
# 핀 모드 설정하기
for segment1 in SEGMENT_PINS1:
    GPIO.setup(segment1, GPIO.OUT)
    GPIO.output(segment1, GPIO.LOW)
    # segment1 GPIO.LOW로 바꾸기
for segment2 in SEGMENT_PINS2:
    GPIO.setup(segment2, GPIO.OUT)
    GPIO.output(segment2, GPIO.LOW)
    # segment2 GPIO.LOW로 바꾸기


time.sleep(5)
print('경보기 작동을 시작합니다.')
#경보기 작동 시작하기

pwm = GPIO.PWM(BUZZER_PIN, 392)
pwm.start(10)
# 버저 핀 솔 음으로 설정하기

try:
    while True:
        val = GPIO.input(PIR_PIN)
        if val == GPIO.HIGH:    #움직임 결과가 1, 움직임이 감지되면
            print('움직임이 감지되었습니다. 경보기 작동을 시작합니다.')
            GPIO.output(LED_PIN, GPIO.HIGH)
            for i in range(6):  # 0~5
                GPIO.output(SEGMENT_PINS1[i], GPIO.HIGH)    #세그먼트 점등하기
            for j in range(5):  # 0~4
                GPIO.output(SEGMENT_PINS2[j], GPIO.HIGH)    #세그먼트 점등하기
            time.sleep(0.5)     #버저 작동
            pwm.ChangeDutyCycle(100)
        else:                   #움직임 결과가 0, 움직임이 감지되지 않으면
            print('움직임이 감지되지 않았습니다.')
            GPIO.output(LED_PIN, GPIO.LOW)
            for k in range(6):
                GPIO.output(SEGMENT_PINS1[k], GPIO.LOW)     #세그먼트 소등하기
            for l in range(5):
                GPIO.output(SEGMENT_PINS2[l], GPIO.LOW)     #세그먼트 소등하기
            pwm.ChangeDutyCycle(0)      #버저 작동 중지
        time.sleep(0.1)


finally:        #정지했을 때
    pwm.stop()
    GPIO.cleanup()
    print('경보기 작동을 중지합니다.')