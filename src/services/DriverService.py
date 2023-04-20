from src.models.Driver import Driver

from src.exts import db


def get_one_from_account(_id) -> Driver:
    rider = Driver.query.filter_by(account_id=_id).first()
    return rider



