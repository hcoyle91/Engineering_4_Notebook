import time
import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
lsm303 = Adafruit_LSM303.LSM303()
# Alternatively you can specify the I2C bus with a bus parameter:
#lsm303 = Adafruit_LSM303.LSM303(busum=2)
# Read the X, Y, Z axis acceleration values and print them.
accel, mag = lsm303.read()
# Grab the X, Y, Z components from the reading and print them out.

mag_x, mag_y, mag_z = mag

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

font = ImageFont.load_default()
top = disp.height
while True:
   accel, mag = lsm303.read()
   accel_x, accel_y, accel_z = accel
   draw.rectangle((0,0,width,height), outline=0, fill=0)
   draw.text((10, top/1.5),f"x: {accel_x/109.69}",  font=font, fill=55)
   draw.text((50, top/3),f"y: {accel_y/109.69}", font=font, fill=55)
   draw.text((80, 2),f"z: {accel_z/109.69}", font=font, fill=55)
   disp.image(image)
   disp.display()
   

# draw.text((x, top),    'Hello',  font=font, fill=255)
# draw.text((x, top+20), 'World!', font=font, fill=255)

disp.image(image)
disp.display()
