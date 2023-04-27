import traceback

from flask import Blueprint, current_app, jsonify, request, abort, make_response
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError

from src import Utils
from src.models.BaseModel import AccountType
import jwt

account_view = Blueprint('account_view', __name__)
BASE_URL = '/account'

from src.services import AccountService as accountService


@account_view.route("/")
def hello():
    return "Hello Welcome to Our API Design for " + current_app.config['ENV']


@account_view.route(BASE_URL + "/request_token", methods=["POST"])
def request_token():
    args = request.get_json()
    phone_number = args.get("phone_number")
    account = accountService.get_one_from_phone_number(phone_number)
    print(account)
    if account:
        return jsonify(
            {
                "logged": True,
                "phone_number": account.phone_number,
                "email": account.email,
                "token": create_access_token(identity=account.id),
            }
        )
    else:
        return make_response(
            {"logged": False, "message": "Could not verify", "status": "Access denied"},
            401,
            {"Authentication": '"login required"'},
        )


@account_view.route(BASE_URL + "/login", methods=["POST"])
def login():
    try:
        auth = request.get_json()
        phone_number = auth.get("phone_number")
        print(phone_number)
        account = accountService.get_one_from_phone_number(phone_number)
        print("****************************************************************")
        if account:
            if account.account_type.upper() == AccountType.RIDER.value.upper():
                return make_response(
                    {"logged": True, "message": "Logged in", "status": "Access granted", "type": "rider",
                     "verification_code": account.verification_code, "token": create_access_token(identity=account.id)}
                )
            else:
                return make_response(
                    {"logged": True, "message": "Logged in", "status": "Access granted", "type": "driver",
                     "verification_code": account.verification_code, "token": create_access_token(identity=account.id)}
                )
        else:
            return make_response(
                {"logged": False, "message": "Could not verify", "status": "Access denied"}
            )
    except Exception as err:
        traceback.print_exc()
        return make_response({"logged": False, "message": "Could not verify", "status": "Access denied"}, 403)


@account_view.route(BASE_URL + '/register', methods=["POST"])
def register():
    data = request.get_json()
    _firstname = data["firstname"]
    _phone_number = data["phone_number"]
    _account_type = data["account_type"]

    try:
        if _account_type.upper() == AccountType.RIDER.value.upper():
            rider = accountService.create_rider(_firstname, _phone_number)
            return jsonify(
                {
                    "logged": True,
                    "rider": rider.to_dict(),
                    "token": create_access_token(identity=rider.id),
                    "verification_code": rider.account.verification_code
                }
            )
        else:
            _firstname = data["firstname"]
            _lastname = data["lastname"]
            _email = data["email"]
            _licence = data["licence_id"]
            _licence_date = data["licence_date"]
            driver = accountService.create_driver(_firstname, _lastname, _email, _phone_number, _licence, _licence_date)
            return jsonify(
                {
                    "logged": True,
                    "driver": driver.to_dict(),
                    "token": create_access_token(identity=driver.id),
                    "verification_code": driver.account.verification_code
                }
            )
    except IntegrityError as ie:
        return jsonify(
            {
                "logged": False,
                "error": True,
                "message": "This number or email is already registered."
            }
        )
    except Exception as e:
        traceback.print_exc()
        return jsonify(
            {
                "logged": False,
                "error": True,
                "message": "Cannot log in! Something happened"
            }
        )