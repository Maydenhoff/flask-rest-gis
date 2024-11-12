from marshmallow import Schema, fields

class WeatherDataResponseSchema(Schema):
    id = fields.Int()
    station_id = fields.Integer(required = True)
    temperature = fields.Float()
    humidity = fields.Float()
    pressure = fields.Float()
    timestamp = fields.DateTime()