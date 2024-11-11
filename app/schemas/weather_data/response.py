from marshmallow import Schema, fields

class WeatherDataResponseSchema(Schema):
    id = fields.Int()
    temperature = fields.Float()
    humidity = fields.Float()
    pressure = fields.Float()
    timestamp = fields.DateTime()