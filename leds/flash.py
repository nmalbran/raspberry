
import time
import sys
from common import Led


def flash(delta=1, channel=2):
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
	d = 1
	try:
		d = float(sys.argv[1])
	except Exception as e:
		pass
	
	flash(delta=d)


