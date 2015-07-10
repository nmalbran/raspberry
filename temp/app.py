from datetime import datetime
from flask import Flask
from flask_restful import Resource, Api
from db import Weather
from weather import get_weather

app = Flask(__name__)
api = Api(app)


class CurrentWeather(Resource):
    def get(self):
        humidity, temperature = get_weather()
        data = {'data': {'temperature': '', 'humidity': ''}}
        if humidity is not None:
            data['data']['humidity'] = str(int(humidity))
        if temperature is not None:
            data['data']['temperature'] = str(int(temperature))
        data['data']['timestamp'] = datetime.strftime(datetime.now(), '%Y-%m-%dT%H:%M:%S')

        return data

class PastDayWeather(Resource):
    def get(self):
        temps = Weather.get_days_stats(1, 60)
        data = {
            'meta': {'rows': len(temps['avg'])},
            'data': temps,
        }
        return data

class PastWeekWeather(Resource):
    def get(self):
        temps = Weather.get_days_stats(7, 1440)
        data = {
            'meta': {'rows': len(temps['avg'])},
            'data': temps,
        }
        return data

class PastMonthWeather(Resource):
    def get(self):
        temps = Weather.get_days_stats(30, 2880)
        data = {
            'meta': {'rows': len(temps['avg'])},
            'data': temps,
        }
        return data


api.add_resource(CurrentWeather, '/cur')
api.add_resource(PastDayWeather, '/day')
api.add_resource(PastWeekWeather, '/week')
api.add_resource(PastMonthWeather, '/month')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
