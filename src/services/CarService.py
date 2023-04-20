from src.models.Car import Car

from src.exts import db


def get_by_id(_id) -> Car:
    return Car.query.filter_by(id=_id).first()


def get_driver_cars(_driver_id):
    return Car.query.filter_by(driver_id=_driver_id)


