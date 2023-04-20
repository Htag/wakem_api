from src.models.Account import Account
from src.models.BaseModel import AccountType
from src.models.RideRequest import RideRequest
from src.models.Rider import Rider

from src.exts import db
from src import Utils


def request(pick_lat, pick_long, drop_lat, drop_long, car_type, rider):
    rq = RideRequest(pick_lat, pick_long, drop_lat, drop_long, car_type=car_type)
    rq.rider = rider
    db.session.add(rq)
