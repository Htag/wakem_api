from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required

car_view = Blueprint('car_view', __name__)
BASE_URL = '/car'

from src.services import CarService as carService
from src.services import CarPositionService as carPositionService

@car_view.route(BASE_URL)
def hello():
    return "Hello CAR API"


@car_view.route(BASE_URL + "/save-position", methods=["POST"])
@jwt_required()
def save_position():
    args = request.get_json()
    car_id = args.get("car")
    lat = args.get("lat")
    long = args.get("long")
    current_user = get_jwt_identity()
    car = carService.get_by_id(current_user)
    carPositionService.save_one_position(lat, long, car)
    print(current_user)
    return {"position": current_user}