from dataclasses import dataclass
from sqlalchemy.orm import relationship
from src.models.BaseModel import BaseModel

from src.app import db


@dataclass
class RiderPosition(db.Model, BaseModel):
    __tablename__ = 'trider_position'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column('id', db.Integer, primary_key=True)
    lat = db.Column('lat', db.Float, nullable=False)
    long = db.Column('long', db.Float, nullable=False)
    # IF IN USE WHEN CHECKING THE POSITION
    user_position_type = db.Column('rider_position_type', db.String(30), nullable=False)

    rider_id = db.Column(db.Integer, db.ForeignKey('trider.id'))
    rider = relationship("Rider", back_populates="rider_positions", order_by="Rider.id")

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
            'user_position_type': self.user_position_type,
        }
