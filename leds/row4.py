
import time
from common import Row4Led, get_cli_float




if __name__ == '__main__':
	r = Row4Led(2,3,16,21)
	d = get_cli_float(1)
	r.bounce(d)
