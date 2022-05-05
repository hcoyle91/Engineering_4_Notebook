from picamera import PiCamera  # Import Time library

from time import sleep
from gpiozero import Button # Import Button library

button = Button(17) # set variable 'button' to be at pin 17
camera = PiCamera() #initializes the camera variable

camera.start_preview()  
frame = 1   #I use this later to number my pictures
button.wait_for_press()
while True:             #This while loop waitsfor the button tobe pressed and t$
    try:                    #It names it based on the variable 'frame' which go$
        camera.capture(f"/home/pi/Documents/Engineering_4_Notebook/Pi_Pictures/Animations/{frame}.jpg")
        frame += 1
        sleep(5)
    except button.when_pressed:       #This breaks the code and stops the camer$
        camera.stop_preview()
        break
