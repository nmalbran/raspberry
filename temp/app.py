from flask import Flask
from db import Weather
import Adafruit_DHT

app = Flask(__name__)

@app.route("/")
def index():
    msg = 'Try again :('
    humidity, temperature = _get_data()
    if humidity is not None and temperature is not None:
        msg = 'Temp={0:0.1f}*C  Humidity={1:0.1f}%\n'.format(temperature, humidity)
    return msg

@app.route("/last")
def last():
    temps = Weather.select().order_by(Weather.timestamp.desc()).limit(100)
    msg = ''
    for w in temps:
        msg += '{0} <br>\n'.format(w)
    return msg


def _get_data(pin=4, sensor=Adafruit_DHT.DHT11):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return humidity, temperature


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
