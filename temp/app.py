from flask import Flask
import Adafruit_DHT
app = Flask(__name__)

@app.route("/")
def hello():
    msg = 'Try again :('
    humidity, temperature = _get_data()
    if humidity is not None and temperature is not None:
        msg = 'Temp={0:0.1f}*C  Humidity={1:0.1f}%\n'.format(temperature, humidity)
    return msg

def _get_data(pin=4, sensor=Adafruit_DHT.DHT11):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return humidity, temperature


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
