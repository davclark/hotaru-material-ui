from __future__ import print_function

from bibliopixel.led import LEDStrip
from bibliopixel.drivers.LPD8806 import DriverLPD8806, ChannelOrder


class Root(object):
    @property
    def greetings(self):
        return [
            Greeting('mundo'),
            Greeting('world')
        ]


class Greeting(object):
    def __init__(self, person):
        self.person = person


class DummyStrip:
    '''Dummy API if we don't have spidev installed

    Real code lives here: 
        https://github.com/ManiacalLabs/BiblioPixel/blob/master/bibliopixel/led.py
    '''

    def fill(self, color):
        pass

    def all_off(self):
        pass

    def update(self):
        pass


class Lights:
    '''BiblioPixel controller'''

    r = 255
    g = 255
    b = 255

    active = None

    def __init__(self):
        # We could also just specify colors in this order in functions like 
        # fill, but this keeps us in a canonical way to specify color
        try:
            self.driver = DriverLPD8806(32, c_order=ChannelOrder.GRB)
            self.strip = LEDStrip(self.driver)
        except ImportError:
            print('** SPI support not available. Running in dummy mode!')
            self.strip = DummyStrip()

        self.off()
        self.active = False

    def on(self, r=None, g=None, b=None):
        if r is not None:
            self.r = int(r)
        if g is not None:
            self.g = int(g)
        if b is not None:
            self.b = int(b)
            
        color = (self.r, self.g, self.b)
        self.strip.fill(color)

        self.strip.update()

        self.active = True

    def off(self):
        self.strip.all_off()

        self.strip.update()

        self.active = False

    def status(self):
        return {'r': self.r,
                'g': self.g,
                'b': self.b,
                'active': self.active,
                }


lights = Lights()
# When we take control of lights, we reset to ensure consistency with internal
# state
lights.off()
