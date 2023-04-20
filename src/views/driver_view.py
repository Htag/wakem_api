from flask import Blueprint, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.models.BaseModel import AccountType

driver_view = Blueprint('driver_view', __name__)
BASE_URL = '/driver'

from src.services import AccountService as accountService
from src.services import DriverService as driverService
from src.services import CarService as carService


@driver_view.route(BASE_URL)
def hello():
    return "Hello DRIVER API"


@driver_view.route(BASE_URL + "/list-my-cars", methods=["POST"])
@jwt_required()
def list_all_my_cars():
    current_user = get_jwt_identity()
    account = accountService.get_by_id(current_user)
    print(current_user)
    if account.account_type == AccountType.DRIVER.value:
        driver = driverService.get_one_from_account(current_user)
        cars = carService.get_driver_cars(driver.id)
        return make_response({'cars': cars})
    else:
        return make_response({'error': True, "errorMessage": "Can't get rider cars"}, 403)
