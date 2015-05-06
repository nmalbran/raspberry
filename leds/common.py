import sys
import time
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


def get_cli_float(argn=1, default=1.0):
    try:
        return float(sys.argv[argn])
    except (IndexError, ValueError) as e:
        return float(default)

class Row4Led(object):
    def __init__(self, c1,c2,c3,c4):
        self.l1 = Led(c1)
        self.l2 = Led(c2)
        self.l3 = Led(c3)
        self.l4 = Led(c4)
        self.row = [self.l1, self.l2, self.l3, self.l4]
        self.off()

    def on(self):
        for l in self.row:
            l.on()

    def off(self):
        for l in self.row:
            l.off()

    def circle(self, delta=0.5):
        i = 0
        while True:
            self.off()
            self.row[i%4].on()
            time.sleep(delta)
            i += 1

    def bounce(self, delta=0.5):
        while True:
            for i in range(4):
                self.off()
                self.row[i].on()
                time.sleep(delta)
            for i in range(2):
                self.off()
                self.row[2-i].on()
                time.sleep(delta)
