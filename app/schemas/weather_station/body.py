from marshmallow import Schema, fields, validates, ValidationError

class CreateWeatherStationBodySchema(Schema):
    name = fields.String(required=True)
    longitude = fields.Float(required=True)
    latitude = fields.Float(required=True)

    @validates('longitude')
    def validate_longitude(self, value):
        if not (-180 <= value <= 180):
            raise ValidationError('Longitude must be between -180 and 180.')

    @validates('latitude')
    def validate_latitude(self, value):
        if not (-90 <= value <= 90):
            raise ValidationError('Latitude must be between -90 and 90.')

class UpdateWeatherStationBodySchema(Schema):
    id = fields.Integer(required= True)
    name = fields.String(required=False)
    longitude = fields.Float(required=False)
    latitude = fields.Float(required=False)

    @validates('longitude')
    def validate_longitude(self, value):
        if not (-180 <= value <= 180):
            raise ValidationError('Longitude must be between -180 and 180.')

    @validates('latitude')
    def validate_latitude(self, value):
        if not (-90 <= value <= 90):
            raise ValidationError('Latitude must be between -90 and 90.')

class GetNearestWeatherStationBodySchema(Schema):
    longitude = fields.Float(required=True)
    latitude = fields.Float(required=True)

    @validates('longitude')
    def validate_longitude(self, value):
        value = float(value)
        if not (-180 <= value <= 180):
            raise ValidationError('Longitude must be between -180 and 180.')
        return value
    
    @validates('latitude')
    def validate_latitude(self, value):
        value = float(value)
        if not (-90 <= value <= 90):
            raise ValidationError('Latitude must be between -90 and 90.')
        return value

