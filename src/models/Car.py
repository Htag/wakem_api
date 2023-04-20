from dataclasses import dataclass
from sqlalchemy.orm import relationship
from src.models.BaseModel import BaseModel

from src.app import db


@dataclass
class Car(db.Model, BaseModel):
    __tablename__ = 'tcar'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column('id', db.Integer, primary_key=True)
    brand = db.Column('brand', db.String(30), nullable=False)
    model = db.Column('model', db.String(50), nullable=False)
    car_type = db.Column('car_type', db.String(30), nullable=False)

    ride_requests = relationship("RideRequest",
                                 order_by="asc(RideRequest.creation_date)",
                                 backref="car_ride_requests")
    car_positions = relationship("CarPosition",
                                 order_by="desc(CarPosition.creation_date)")
    driver_id = db.Column(db.Integer, db.ForeignKey('tdriver.id'))
    driver = relationship("Driver", back_populates="cars")

    def to_dict(self):
        if self is None:
            return None
        return {
            'id': self.id,
            'brand': self.brand,
            'model': self.model,
            'car_type': self.car_type,
            'ride_requests': [r.to_dict() for r in self.ride_requests],
            'car_positions': [p.to_dict() for p in self.car_positions],
            'driver': self.driver.to_dict()
        }