from lcd import drivers
import time
import datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHT_PIN = 4


display = drivers.Lcd()
now=datetime.datetime.now()

try:
    while True :
        print("Writing to display")
        now=datetime.datetime.now()
        display.lcd_display_string(now.strftime("%x%X"),1)
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        display.lcd_display_string('%.1f*C, %.1f%%' % (t,h),2)
finally:
    print("Cleaning up!")
    display.lcd_clear()
