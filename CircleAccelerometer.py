import time    #imports time library and other libraries for accelerometer (LSM303) and OLED display (SSD1306)
import Adafruit_LSM303        
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24    #Sets the pin configuration for the rasberry Pi
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
lsm303 = Adafruit_LSM303.LSM303()

# Read the X, Y, Z axis acceleration values and print them.
accel, mag = lsm303.read()
# Grab the X, Y, Z components from the reading and print them out.

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d) #Sets variable disp to read where the accelerometer is reading (0x3d)
disp.begin()   # Initializes the display off the OLED
disp.clear()
disp.display()
width = disp.width   # Creates variables set to the height and width of the OLED to help organize on the screen
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)     # draw is initialized as image which is the bounds of height and width
draw.rectangle((0,0,width,height), outline=0, fill=0) #Draws a black rectangle over the screen to make sure it is clear

font = ImageFont.load_default()  # Sets the font for any writing on the display
# top = disp.height
while True:                # A loop that reads the accelerometer values( acceleration in the x and y coordinates of the chip). Then draws a rectangle to reset the screen
   accel, mag = lsm303.read()       # Then the loop sets two variables to equal the accelerometer values of x and y accelerations and draw an elipse based on those variables.
   accel_x, accel_y, accel_z = accel
   draw.rectangle((0,0,width,height), outline=0, fill=0)
   yCoor = round((-2*accel_x/109.69), 0)+32
   xCoor = round((-3*accel_y/109.69), 0)+64
   draw.ellipse((xCoor, yCoor, xCoor+10, yCoor+10), outline=255, fill=0) 
   disp.image(image)    #initializes display again
   disp.display()
   time.sleep(.000001)  # A very small sleep period in the loop so the loop does not go too fast and only show the black rectangle.
   

# draw.text((x, top),    'Hello',  font=font, fill=255)
# draw.text((x, top+20), 'World!', font=font, fill=255)

disp.image(image)
disp.display()
