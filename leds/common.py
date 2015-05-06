import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

class Led(object):
    def __init__(self, channel):
        self.channel = channel
        RPi.GPIO.setup(self.channel, RPi.GPIO.OUT)

    def __del__(self):
        RPi.GPIO.cleanup(self.channel)

    def on(self):
        RPi.GPIO.output(self.channel, True)

    def off(self):
        RPi.GPIO.output(self.channel, False)
