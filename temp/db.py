from datetime import datetime
from peewee import *

db = SqliteDatabase('temp.db')

class Weather(Model):
    timestamp = DateTimeField(default=datetime.now)
    temperature = FloatField()
    humidity = FloatField()

#    def __str__(self):
#        return "" % (self.temperature, self.humidity)

    class Meta:
        database = db


def create_db():
    db.connect()
    db.create_tables([Weather])
