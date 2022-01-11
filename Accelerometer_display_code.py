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
accel_x, accel_y, accel_z = accel
mag_x, mag_y, mag_z = mag
   
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

font = ImageFont.load_default()

while True:
  draw.text((x, top),    accel_x,  font=font, fill=255)
  draw.text((x, top+20), accel_y, font=font, fill=255)
  draw.text((x, top+20), accel_y, font=font, fill=255)


# draw.text((x, top),    'Hello',  font=font, fill=255)
# draw.text((x, top+20), 'World!', font=font, fill=255)

disp.image(image)
disp.display()
