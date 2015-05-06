
import time
import sys
from common import Led, get_cli_float


def blink(delta=1, channel=2):
	led = Led(channel)
	while True:
		try:
			led.on()
			time.sleep(delta)
			led.off()
			time.sleep(delta)
		except KeyboardInterrupt as e:
			print('Finished')
			break


def blink2(delta=1, c1=2, c2=3):
	led1 = Led(c1)
	led2 = Led(c2)
	while True:
		try:
			led1.on()
			led2.off()
			time.sleep(delta)
			led1.off()
			led2.on()
			time.sleep(delta)
		except KeyboardInterrupt as e:
			print('Finished')
			break


if __name__ == '__main__':
	delta = get_cli_float(1, 1.0)
	blink2(delta)


