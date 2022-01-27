import time
import picamera
effect_arr = ['negative', 'solarize', 'sketch', 'denoise', 'cartoon']
name_arr = ['picture1.jpg', 'picture2.jpg', 'picture3.jpg', 'picture4.jpg', 'picture5.jpg']
i = 0
x = 0
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    print("Running...")
    for x in range(5):
        time.sleep(.1)
        camera.image_effect = effect_arr[i]
        camera.capture(name_arr[x])
        print("Another picture taken")
        i +=1
        x +=1
