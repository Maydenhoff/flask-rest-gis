from . import db
from geoalchemy2 import Geometry
from sqlalchemy.orm import relationship
from .weather_data import WeatherData 

class WeatherStation(db.Model):
    __tablename__ = 'weather_stations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(Geometry('POINT', srid=4326),  nullable=False)

    weather_data = relationship("WeatherData", backref="station", cascade="all, delete-orphan" )