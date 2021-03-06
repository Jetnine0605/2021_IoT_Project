import spidev
import RPi.GPIO as GPIO
import time

LED_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# SPI 인스턴스 생성
spi = spidev.SpiDev()

# SPI 통신 시작
spi.open(0, 0)  # bus : 0, dev : 0

# SPI 통신 속도 설정
spi.max_speed_hz = 1000000

# 채널에서 SPI 데이터 읽기 (0~1023)
def analog_read(channel):
    # [byte_1, byte_2, byte_3]
    # byte_2 : channed config(channel 0) (+8) -> 0000 1000 -> 1000 0000
    ret = spi.xfer2([1, ( 8 +channel) << 4, 0])
    print(ret)
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True :
        reading = analog_read(0)   # reading(0~1023)
        print("Reading=%d" % reading)
        if reading<512:
            print('값이 512보다 작습니다. LED를 켭니다')
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
finally:
    spi.close()
    GPIO.cleanup()
    print('Cleanup and exit')