from flask import Flask
from config import Config
from .controllers.weather_station import weather_station_bp
from .models import db
from .schemas import ma

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    ma.init_app(app)    
    
    db.init_app(app)
    app.register_blueprint(weather_station_bp, url_prefix='/weather-station')

    return app
