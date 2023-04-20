from dataclasses import dataclass
from sqlalchemy import ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship, backref
from src.models.BaseModel import BaseModel

from src.app import db


@dataclass
class Driver(db.Model, BaseModel):
    __tablename__ = 'tdriver'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column('id', db.Integer, primary_key=True)
    licence = db.Column('licence', db.String(50), nullable=False)
    licence_date = db.Column('licence_date', db.Date, nullable=False)
    rating = db.Column('rating', db.Float)

    account_id = db.Column(db.Integer, db.ForeignKey('taccount.id'), unique=True)
    account = relationship("Account", backref=backref("rider", uselist=False))
    cars = relationship("Car", order_by="desc(Car.model)")
    ride_requests = relationship("RideRequest",
                                 order_by="asc(RideRequest.creation_date)",
                                 back_populates="driver")

    def __init__(self, license_id, license_date):
        self.licence = license_id
        self.licence_date = license_date
        self.rating = 5

    def to_dict(self):
        if self is None:
            return None
        return {
            'id': self.id,
            'licence': self.licence,
            'licence_date': self.licence_date,
            'rating': self.rating,
            'account': self.account.to_dict(),
            'account_id': self.account_id,
            'cars': [car.to_dict() for car in self.cars],
            'ride_requests': [ride_request.to_dict() for ride_request in self.ride_requests]
        }

    def is_active(self):
        return self.account.enabled
