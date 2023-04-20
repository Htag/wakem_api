from dataclasses import dataclass

from sqlalchemy.orm import relationship

from src.app import db

from src import Utils
from src.models.BaseModel import BaseModel, AccountType



@dataclass
class Account(db.Model, BaseModel):
    __tablename__ = 'taccount'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.String(255), nullable=True, unique=True)
    phone_number = db.Column('phone_number', db.String(255), nullable=False, unique=True)
    firstname = db.Column('firstname', db.String(50), nullable=False)
    lastname = db.Column('lastname', db.String(50), nullable=True)
    birthday = db.Column('birthday', db.Date, nullable=True)
    balance = db.Column('balance', db.Integer, nullable=False, default=0)
    account_type = db.Column('user_type', db.String(50), default=AccountType.RIDER.value)
    verification_code = db.Column('verification_code', db.String(4))
    mail_confirmed = db.Column('mail_confirmed', db.Boolean, default=False)
    phone_confirmed = db.Column('phone_confirmed', db.Boolean, default=False)
    enabled = db.Column('enabled', db.Boolean, default=True)

    # rider = relationship("Rider", uselist=False, backref="account")
    # driver = relationship("Driver", uselist=False, backref="account")

    def __init__(self,phone_number, firstname, account_type):
        self.phone_number = phone_number
        self.firstname = firstname
        self.balance = 0
        self.account_type = account_type
        self.enabled = True
        self.verification_code = Utils.generate_code()

    @staticmethod
    def clone_from(phone_number, firstname, balance, account_type, enabled):
        account = Account(phone_number, firstname, account_type)
        account.balance = balance
        account.enabled = enabled
        account.verification_code = Utils.generate_code()
        return account

    def to_dict(self):
        if self is None:
            return None
        return {
            "id": self.id,
            "firstname": self.firstname,
            "phone_number": self.phone_number,
            "email": self.email,
            "enabled": self.enabled
        }
