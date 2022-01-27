import time  # imports time library
import picamera
effect_arr = ['negative', 'solarize', 'sketch', 'denoise', 'cartoon']       #Creates two arrays one haveing the different effects  
name_arr = ['picture1.jpg', 'picture2.jpg', 'picture3.jpg', 'picture4.jpg', 'picture5.jpg']     #the other having names to be assignned to the 5 pictures
i = 0
x = 0
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)     #Intitializes The Pi camera
    camera.start_preview()
    print("Running...")
    for x in range(5):                  # A for loops to take five pics with different affects
        time.sleep(.1)
        camera.image_effect = effect_arr[i]     
        camera.capture(name_arr[x])
        print("Another picture taken")          # Prints after the camera takes each picture
        i +=1
        x +=1
