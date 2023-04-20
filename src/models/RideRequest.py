from dataclasses import dataclass
from sqlalchemy import ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship
from src.models.BaseModel import BaseModel

from src.app import db
from src.models.Payment import Payment


@dataclass
class RideRequest(db.Model, BaseModel):
    __tablename__ = 'tride_request'

    id = db.Column('id', db.String, primary_key=True)
    pickup_location_lat = db.Column('pickup_location_lat', db.Float)
    pickup_location_long = db.Column('pickup_location_long', db.Float)
    pickup_time = db.Column('pickup_time', db.DateTime, nullable=True)
    dropoff_location_lat = db.Column('dropoff_location_lat', db.Float)
    dropoff_location_long = db.Column('dropoff_location_long', db.Float)
    dropoff_time = db.Column('dropoff_time', db.DateTime, nullable=True)
    car_type = db.Column('car_type', db.String)
    rate = db.Column('rate', db.Integer)
    rate_comment = db.Column('rate_comment', db.Text)

    driver_id = db.Column(db.Integer, db.ForeignKey('tdriver.id'))
    driver = relationship("Driver", back_populates="ride_requests")
    rider_id = db.Column(db.Integer, db.ForeignKey('trider.id'))
    rider = relationship("Rider", back_populates="ride_requests")
    car_id = db.Column(db.Integer, db.ForeignKey('tcar.id'))
    car = relationship("Car", back_populates="ride_requests", viewonly=True)
    payments = relationship("Payment",
                            order_by="desc(Payment.creation_date)",
                            primaryjoin="RideRequest.id == Payment.ride_request_id",
                            backref="ride_request_payments")

    def __init__(self, pickup_location_lat, pickup_location_long, dropoff_location_lat, dropoff_location_long, car_type):
        self.pickup_location_lat = pickup_location_lat
        self.pickup_location_long = pickup_location_long
        self.dropoff_location_lat = dropoff_location_lat
        self.dropoff_location_long = dropoff_location_long
        self.car_type = car_type

    def to_dict(self):
        if self is None:
            return None
        return {
            'id': self.id,
            'pickup_location_lat': self.pickup_location_lat,
            'pickup_location_long': self.pickup_location_long,
            'pickup_time': self.pickup_time,
            'dropoff_location_lat': self.dropoff_location_lat,
            'dropoff_location_long': self.dropoff_location_long,
            'dropoff_time': self.dropoff_time,
            'car_type': self.car_type,
            'rate': self.rate,
            'rate_comment': self.rate_comment,
            'driver_id': self.driver_id,
            'driver': self.driver.to_dict(),
            'rider_id': self.rider_id,
            'rider': self.rider.to_dict()
        }
