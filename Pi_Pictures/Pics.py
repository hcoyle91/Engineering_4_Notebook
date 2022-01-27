import time
import picamera
effect_arr = ['negative', 'solarize', 'sketch', 'denoise', 'cartoon']
i = 0
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    print("Running...")
    for x in range(5)
        time.sleep(.1)
        camera.image_effect = effect_arr[i]
        camera.capture('Picture2.jpg')
        print("Another picture taken")
        i++
