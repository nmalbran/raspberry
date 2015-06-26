from datetime import datetime
import peewee as pw
from marshmallow import Schema, fields

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
    def to_dict_list(cls, weather_list):
        schema = WeatherSchema(many=True)
        return schema.dump(weather_list).data


class WeatherSchema(Schema):
    timestamp = fields.DateTime()
    temperature = fields.Number()
    humidity = fields.Number()


def create_db():
    db.connect()
    db.create_tables([Weather])
