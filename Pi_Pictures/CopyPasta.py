from picamera import PiCamera  # Import Time library
from time import sleep
from gpiozero import Button # Import Button library

button = Button(17) # set variable 'button' to be at pin 17
camera = PiCamera() #initializes the camera variable

camera.start_preview()  
frame = 1   #I use this later to number my pictures
while True:             #This while loop waitsfor the button tobe pressed and then 'captures' a picture and stores it in the specified path. 
    try:                    #It names it based on the variable 'frame' which goes up by one every loop.
        button.wait_for_press()
        camera.capture(f"/home/pi/Documents/Engineering_4_Notebook/Pi_Pictures/Animations/{frame}.jpg")
        frame += 1
    except KeyboardInterrupt:       #This breaks the code and stops the camera if there is any interupt from the user/keyboard
        camera.stop_preview()
        break
