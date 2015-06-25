
from db import Weather
import Adafruit_DHT
#from dht11 import dht11_Module


sensor = Adafruit_DHT.DHT11
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).  
# If this happens try again!
if humidity is not None and temperature is not None:
    #print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
    w = Weather.create(temperature=temperature, humidity=humidity)


#dht11 = dht11_Module(pin)
#result = dht11.getData()      
#print "Humidity:    %d%%" % result['humidity']
#print "Temperature: %dC"  % result['temperature']
#if result['temperature'] is not None and result['humidity'] is not None:
#    w = Weather.create(temperature=result['temperature'], humidity=result['humidity'])


