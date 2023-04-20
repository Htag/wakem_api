from src.models.Rider import Rider
from src.models.RiderPosition import RiderPosition

from src.exts import db


def save_one_position(lat: float, long: float, rider):
    rider_position = RiderPosition(lat, long)
    rider_position.rider = rider
    db.session.add(rider_position)
    return rider_position


def save_all_position(positions):
    db.session.add(positions)

