from enum import Enum
import logging
from src.exts import db
from sqlalchemy.sql import func
import uuid


class UserStatusEnum(Enum):
    ACTIVE = "active"
    DISABLED = "disabled"


class StatusEnum(Enum):
    COMPLETE = "completed"
    ONGOING = "ongoing"
    GAVEUP = "gave up"


class AccountType(Enum):
    RIDER = "rider"
    DRIVER = "driver"


class PaymentType(Enum):
    CASH = "cash"
    WALLET = "wallet"
    THIRD_PARTY = "third_party"


class CarPositionType(Enum):
    USER_DEFINED = "user_defined"
    OTHER = "other"


class BaseModel:
    log = logging.getLogger(__name__)
    creation_date = db.Column('creation_date', db.Date, server_default=func.now())


    @staticmethod
    def get_uuid():
        return str(uuid.uuid4())