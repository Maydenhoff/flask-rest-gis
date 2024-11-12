from marshmallow import Schema, fields

class CreateWatherDataBodySchema(Schema):
    station_id = fields.Integer(required = True)
    temperature = fields.Float(required = True)
    humidity = fields.Float(required = True)
    pressure = fields.Float(required = True)

