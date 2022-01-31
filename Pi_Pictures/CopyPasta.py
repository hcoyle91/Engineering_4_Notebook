from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()

camera.start_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.capture(f"/home/pi/Documents/Engineering_4_Notebook/Pi_Pictures/Animations/{frame}.jpg")
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break
