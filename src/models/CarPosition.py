from dataclasses import dataclass
from sqlalchemy.orm import relationship
from src.models.BaseModel import BaseModel, CarPositionType

from src.app import db


@dataclass
class CarPosition(db.Model, BaseModel):

    __tablename__ = 'tcar_position'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column('id', db.Integer, primary_key=True)
    lat = db.Column('lat', db.Float, nullable=False)
    long = db.Column('long', db.Float, nullable=False)
    # IF IN USE WHEN CHECKING THE POSITION
    car_position_type = db.Column('car_position_type', db.String(30), nullable=False, default=CarPositionType.OTHER.value)

    car_id = db.Column(db.Integer, db.ForeignKey('tcar.id'))
    car = relationship("Car", back_populates="car_positions", order_by="Car.model")

    def __int__(self, lat, long):
        self.lat = lat
        self.long = long

    def to_dict(self):
        if self is None:
            return None
        return {
            'id': self.id,
            'lat': self.lat,
            'long': self.long,
            'car_position_type': self.car_position_type,
        }
