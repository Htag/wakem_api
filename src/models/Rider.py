from dataclasses import dataclass
from sqlalchemy import ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship, backref
from src.models.BaseModel import BaseModel

from src.app import db


@dataclass
class Rider(db.Model, BaseModel):
    __tablename__ = 'trider'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column('id', db.Integer, primary_key=True)

    # one-to-many
    addresses = relationship("Address", order_by="desc(Address.name)", backref="rider_addresses")
    ride_requests = relationship("RideRequest", order_by="asc(RideRequest.creation_date)")
    account_id = db.Column(db.Integer, db.ForeignKey('taccount.id'), unique=True)
    account = relationship("Account", backref=backref("rider_account", uselist=False))
    rider_positions = relationship("RiderPosition",
                                   order_by="desc(RiderPosition.creation_date)")

    def __int__(self, account, addresses, ride_requests):
        self.account_id = account.id
        self.account = account
        self.addresses = addresses
        self.ride_requests = ride_requests

    def to_dict(self):
        if self is None:
            return None
        return {
            'id': self.id,
            'account_id': self.account_id,
            'account': self.account.to_dict(),
            'addresses': [address.to_dict() for address in self.addresses],
            'ride_requests': [ride_request.to_dict() for ride_request in self.ride_requests]
        }

    def is_active(self):
        return self.account.enabled
