from src.models.Account import Account
from src.models.BaseModel import AccountType
from src.models.Driver import Driver
from src.models.Rider import Rider

from src.exts import db
from src import Utils


def create_rider(_firstname, _phone_number) -> Rider:
    account = Account.clone_from(firstname=_firstname, phone_number=_phone_number,
                                 account_type=AccountType.RIDER.value, balance=0, enabled=True)
    rider = Rider()
    rider.enabled = False
    rider.account_id = account.id
    rider.account = account
    db.session.add(account, rider)
    db.session.commit()
    return rider


def create_driver(_firstname, _lastname, _email, _phone_number, license_id,
                  license_date) -> Driver:
    account = Account(firstname=_firstname, phone_number=_phone_number,
                      account_type=AccountType.DRIVER.value)
    account.email = _email
    account.lastname = _lastname
    account.enabled = True

    driver = Driver(license_id, license_date)
    driver.account = account
    driver.account_id = account.id
    db.session.add(account, driver)
    db.session.commit()
    return driver


def get_all():
    accounts = Account.query.all()
    print(accounts)
    return accounts


def get_by_id(_id) -> Account:
    return Account.query.filter_by(id=_id).first()


def get_one_from_id(_id) -> Account:
    u: Account = Account.query.filter_by(id=_id).first()
    return u


def get_one_from_phone_number(_phone_number) -> Account:
    u: Account = Account.query.filter_by(phone_number=_phone_number).first()
    return u


def get_current_account_from_id(_id):
    u: Account = Account.query.filter_by(id=_id).first()
    u.fullname = Utils.full_name_from_account(u)
    return u


def get_account_from_email(_email):
    account = Account.query.filter_by(email=_email).first()
    return account


def get_one_from_email_and_password(_email, _password):
    u = Account.query.filter_by(Accountname=_email, password=_password).first()
    return u
