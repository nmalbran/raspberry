import math
from datetime import datetime, timedelta
import peewee as pw
from marshmallow import Schema, fields

TSFORMAT = '%Y-%m-%dT%H:%M:%S'

db = pw.SqliteDatabase('temp.db')


class Weather(pw.Model):
    timestamp = pw.DateTimeField(default=datetime.now)
    temperature = pw.FloatField()
    humidity = pw.FloatField()

    def get_formatted_ts(self):
        return "%d/%d/%d %d:%d:%d" % (self.timestamp.year, self.timestamp.month, self.timestamp.day, self.timestamp.hour, self.timestamp.minute, self.timestamp.second)

    def __str__(self):
        #ts = datetime.strftime("%H:%M:%S", self.timestamp)
        return "%s | T %d*C | H %d%%" % (self.get_formatted_ts(), self.temperature, self.humidity)

    class Meta:
        database = db
    
    def to_dict(self):
        schema = WeatherSchema()
        return schema.dumps(self).data

    @classmethod
    def format_ts(cls, ts, format='%d/%m %H:%M'):
        dt = datetime.strptime(ts, TSFORMAT)
        return dt.strftime(format)

    @classmethod
    def to_dict_list(cls, weather_list):
        schema = WeatherSchema(many=True)
        return schema.dump(weather_list).data

    @classmethod
    def prepare_to_graph(cls, weather_list, cluster=10):
        n = len(weather_list)
        n_clusters = int(math.ceil(n*1.0/cluster))
        
        data_clusters = [[] for i in range(n_clusters)]
        for i in range(n):
            data_clusters[i/cluster].append(weather_list[i])

        data = {
            'timestamp': [],
            'min': [],
            'avg': [],
            'max': [],
        }
        for c in data_clusters:
            temp = [w['temperature'] for w in c]
            data['min'].append(min(temp))
            data['avg'].append(sum(temp)/len(temp))
            data['max'].append(max(temp))
            data['timestamp'].append(cls.format_ts(c[len(temp)/2]['timestamp']))

        return data

    @classmethod
    def get_days_stats(cls, days, cluster=60):
        ago = datetime.now() - timedelta(days=days)
        ago = ago.replace(minute=0, second=0, microsecond=0)
        weathers = Weather.select().where(Weather.timestamp >= ago).order_by(Weather.timestamp)
        return cls.prepare_to_graph(Weather.to_dict_list(weathers), cluster)

class WeatherSchema(Schema):
    timestamp = fields.DateTime(format=TSFORMAT)
    temperature = fields.Number()
    humidity = fields.Number()


def create_db():
    db.connect()
    db.create_tables([Weather])
