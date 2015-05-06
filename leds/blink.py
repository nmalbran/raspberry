
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


if __name__ == '__main__':
	delta = get_cli_float(1, 1.0)
	blink(delta)


