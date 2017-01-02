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

class Lights:
    '''BiblioPixel controller'''

    r=255
    g=255
    b=255

    active = None

    def __init__(self):
        # We could also just specify colors in this order in functions like 
        # fill, but this keeps us in a canonical way to specify color
        self.driver = DriverLPD8806(32, c_order=ChannelOrder.GRB)
        self.strip = LEDStrip(self.driver)

        self.off()
        self.active = False

    def on(self):
        color = (self.r, self.g, self.b)
        self.strip.fill(color)

        # XXX check return value?
        self.strip.update()

        self.active = True

    def off(self):
        self.strip.all_off()

        # XXX check return value?
        self.strip.update()

        self.active = False

    def status(self):
        return {'r': self.r,
                'g': self.g,
                'b': self.b,
                'active': self.active,
                }

lights = Lights()
