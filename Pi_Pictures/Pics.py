import time
import picamera

with picamera.PiCamera() as camera:
    print("Running...")
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('Picture2.jpg')
    print("All done, picture taken")
