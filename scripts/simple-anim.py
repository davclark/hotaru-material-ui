#!/home/pi/pixelenv/bin/python

from bibliopixel.led import LEDStrip
from bibliopixel.drivers.LPD8806 import DriverLPD8806, ChannelOrder
from bibliopixel.animation import StripChannelTest

# You can check if the color order is correct using this animation
driver = DriverLPD8806(32, c_order=ChannelOrder.GRB)
strip = LEDStrip(driver)
anim = StripChannelTest(strip)
anim.run()
