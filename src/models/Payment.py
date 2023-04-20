from dataclasses import dataclass
from sqlalchemy.orm import relationship
from src.models.BaseModel import BaseModel, PaymentType

from src.app import db


@dataclass
class Payment(db.Model, BaseModel):
    __tablename__ = 'tpayment'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column('id', db.Integer, primary_key=True)
    amount = db.Column('amount', db.Float, nullable=False)
    payment_type = db.Column('payment_type', db.String, nullable=False, default=PaymentType.CASH)
    payment_date = db.Column('payment_date', db.Date, nullable=False)
    rate = db.Column('rate', db.Float, nullable=False)

    ride_request_id = db.Column(db.String, db.ForeignKey('tride_request.id'))
    ride_request = relationship("RideRequest", viewonly=True)

    def __init__(self, payment_date, amount, rate, account_id):
        self.payment_date = payment_date
        self.amount = amount
        self.rate = rate
        self.account_id = account_id
