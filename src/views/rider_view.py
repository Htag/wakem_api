from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

rider_view = Blueprint('rider_view', __name__)
BASE_URL = '/rider'


from src.services import RiderService as riderService
from src.services import RiderPositionService as riderPositionService
from src.services import RideRequestService as rideRequestService


@rider_view.route(BASE_URL)
def hello():
    return "Hello RIDER API"


@rider_view.route(BASE_URL + "/save-position", methods=["POST"])
@jwt_required()
def save_position():
    args = request.get_json()
    lat = args.get("lat")
    long = args.get("long")
    current_user = get_jwt_identity()
    rider = riderService.get_one_from_account(current_user)
    riderPositionService.save_one_position(lat, long, rider)
    print(current_user)
    return {"position": current_user}


@jwt_required()
@rider_view.route(BASE_URL + "/request-ride", methods=["POST"])
def request_ride(current_user):
    current_user = get_jwt_identity()
    rider = riderService.get_one_from_account(current_user)
    ride_request = rideRequestService.request(rider)
    return ""
