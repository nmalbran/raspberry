import Adafruit_DHT

def get_weather(pin=4, sensor=Adafruit_DHT.DHT11):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return humidity, temperature


