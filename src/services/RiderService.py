from src.models.Rider import Rider
from src.models.Address import Address

from src.exts import db


def get_one_from_account(_id) -> Rider:
    rider = Rider.query.filter_by(account_id=_id).first()
    return rider


def get_favorite_addresses(rider_id):
    return Address.query.filter_by(rider_id=rider_id, favorite=True).all()
