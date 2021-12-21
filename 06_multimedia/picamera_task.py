import picamera
import time

path = '/home/pi/src4/06_multimedia/'

camera = picamera.PiCamera()
now_str = time.strftime("%Y%m%d_%H%M%S")

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3)   # 카메라 준비시간
    while True:
        val = input("photo:1, video:2, exit:9 >")
        if val == '1':
            print('사진 촬영')
            #camera.capture('%sphoto_%s.jpg' % (path, now_str))
            camera.capture('/home/pi/src4/06_multimedia/photo_%s.jpg' % now_str)
        elif val == '2':
            camera.start_recording('%svideo_%s.h264' % (path, now_str))
            input("press enter to stop recording..")
            camera.stop_recording()
            print('동영상 촬영')
        elif val =='9':
            break
        else:
            print("incorrect command")
finally: 
    camera.stop_preview()