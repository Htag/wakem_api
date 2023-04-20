from dataclasses import dataclass
from sqlalchemy.orm import relationship
from src.models.BaseModel import BaseModel

from src.app import db


@dataclass
class Address(db.Model, BaseModel):

    __tablename__ = 'taddress'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column('id', db.String, primary_key=True)
    name = db.Column('name', db.String(150), nullable=False)
    lat = db.Column('lat', db.Float, nullable=False)
    long = db.Column('long', db.Float, nullable=False)
    favorite = db.Column('favorite', db.Boolean, default=False)
    address_type = db.Column('address_type', db.String(150), nullable=False)

    rider_id = db.Column(db.Integer, db.ForeignKey('trider.id'))
    rider = relationship("Rider", viewonly=True)

    def __init__(self, name, lat, long, address_type):
        self.name = name
        self.lat = lat
        self.long = long
        self.address_type = address_type

    def to_dict(self):
        if self is None:
            return None
        return {
            'id': self.id,
            'name': self.name,
            'lat': self.lat,
            'long': self.long,
            'address_type': self.address_type
        }
