from src.models.Car import Car
from src.models.CarPosition import CarPosition

from src.exts import db


def save_one_position(lat: float, long: float, car):
    car_position = CarPosition(lat, long)
    car_position.car = car
    db.session.add(car_position)
    return car_position


def save_all_position(positions):
    db.session.add(positions)
