from marshmallow import Schema, fields, post_dump
from ..weather_data.response import WeatherDataResponseSchema
from geoalchemy2.shape import to_shape
from geoalchemy2 import WKBElement

class WeatherStationResponseSchema(Schema):
    id = fields.Int()
    name = fields.String(required=True)
    longitude = fields.Float(required=False)
    latitude = fields.Float(required=False)
    location = fields.String(required=False)
    weather_data = fields.Nested(WeatherDataResponseSchema, many = True)
    
    @post_dump
    def convert_location_to_lat_and_lot(self, data, **kwargs):
        location = data.get("location")
        
        print(data)
        if location:
            point = to_shape(WKBElement(location)) 
            data["latitude"] = point.y
            data["longitude"] = point.x
            
        return data 
    