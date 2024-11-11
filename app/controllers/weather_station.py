from flask import Blueprint, jsonify, request
from ..models.weather_station import WeatherStation
from ..models import db
from geoalchemy2.shape import to_shape
from ..schemas.weather_station.response import WeatherStationResponseSchema
from geoalchemy2.elements import WKTElement
from geoalchemy2.functions import ST_Distance 
from ..schemas.weather_station.body import CreateWeatherStationBodySchema, UpdateWeatherStationBodySchema, GetNearestWeatherStationBodySchema

weather_station_bp = Blueprint('weather-station', __name__)

@weather_station_bp.route('/', methods=['GET'])
def get_all():
    stations = db.session.query(WeatherStation).order_by(WeatherStation.id).all()
    schema = WeatherStationResponseSchema(many=True)
    response = schema.dump(stations)
    print(response)
    
    return jsonify({"weather_stations":response})


@weather_station_bp.route('/', methods=['POST'])
def create():
    body = request.get_json()
    schema = CreateWeatherStationBodySchema()
    errors = schema.validate(body)

    if errors:
        return jsonify(errors), 400
    
    name = body["name"]
    if (db.session.query(WeatherStation).filter_by(name = name ).first()):
        return jsonify({"error":"Weather station ya existente con ese nombre."})
    
    data = schema.load(body)
    longitude = data["longitude"]
    latitude = data["latitude"]
    location = WKTElement(f"POINT({longitude} {latitude})", srid= 4326)

    new_weather_station = WeatherStation(name = name, location=location)


    db.session.add(new_weather_station)
    db.session.commit()


    return jsonify({"id": new_weather_station.id}), 201


    
@weather_station_bp.route("/update", methods=['PUT'])
def update():
    body = request.get_json()
    schema = UpdateWeatherStationBodySchema()
    errors = schema.validate(body)
    
    if errors:
        return jsonify(errors), 400

    data = schema.load(body)

    weather_station = db.session.query(WeatherStation).get(data["id"])
 
    if not weather_station:
        return jsonify({"error": f"Weather station con id {data['id']} no encontrada."}), 404

    point = to_shape(weather_station.location)

    weather_station.name = data.get("name", weather_station.name)
    new_latitude = data.get("latitude", point.y)
    new_longitude = data.get("longitude", point.x)

    weather_station.location = WKTElement(f"POINT({new_longitude} {new_latitude})", srid= 4326)
    
    db.session.commit()

    return jsonify({"message": "Estacion metereologica actualizada con exito.", "id":weather_station.id})


@weather_station_bp.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    weather_station = db.session.query(WeatherStation).get(id)
    
    if not weather_station:
        return jsonify({"error": f"Weather station con id {id} no encontrada."}), 404
    

    db.session.delete(weather_station)
    db.session.commit()

    return jsonify({"message": f"Weather station con id {id} eliminada con exito"})



@weather_station_bp.route("/nearest", methods=["GET"])
def nearest():
    longitude = request.args.get('long')
    latitude = request.args.get('lat')
    schema = GetNearestWeatherStationBodySchema()
    errors = schema.validate({"longitude": float(longitude), "latitude": float(latitude)})
    
    if errors:
        return jsonify(errors), 400

    data = schema.load({"longitude": float(longitude), "latitude": float(latitude)})

    point= WKTElement(f"POINT({data['longitude']} {data['latitude']})", srid= 4326)
    
    nearest_station = db.session.query(WeatherStation).order_by(ST_Distance(WeatherStation.location, point)).first()
    
    response_schema = WeatherStationResponseSchema()
    print(nearest_station)
    response = response_schema.dump(nearest_station)
    print(response)
    
    return jsonify({"weather_stations":response})


