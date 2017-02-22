#!/home/pi/pixelenv/bin/python

from sys import argv

from bibliopixel.led import LEDStrip
from bibliopixel.drivers.LPD8806 import DriverLPD8806, ChannelOrder

# You can check if the color order is correct using this animation
driver = DriverLPD8806(32, c_order=ChannelOrder.GRB)
strip = LEDStrip(driver)
color_ints = tuple(int(x) for x in argv[1:])
strip.fill(color_ints)
strip.update()
