## Henry Coyle - servo bluetooth code
from gpiozero import Servo
from time import sleep
from gpiozero import Button


button2 = Button(17)
button = Button(16)
val =-1
myGPIO=25
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
 
servo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)



#try:
servo.value = -1
while True:
	if button.is_pressed:
		print("turning left")
		servo.value = servo.value + .09
		sleep(.1)
	if button2.is_pressed:
		print("Turning right")
		servo.value = servo.value - .09
		sleep(.1)
	if servo.value>.9:
		servo.value = -1
	if servo.value<-.9:
		servo.value = 1
#except KeyboardInterrupt:
#	print("Stopping")


