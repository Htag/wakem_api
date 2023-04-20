import datetime
import random
from json import JSONEncoder
import re
import dateutil.parser


TOKEN_EXPIRATION = 120
SECRET_KEY = "06a4c153fd27af256816c38fedab75a9"
HASH_VALUE = "HS256"


def generate_code():
    return str(random.randint(1000, 9999))


def full_name_from_account(account):
    fname = str(account.account_info.firstname + account.account_info.lastname)
    full_name = fname.replace(' ', '')
    return full_name


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


class DateTimeEncoder(JSONEncoder):
        # Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()


def decode_datetime(empDict):
   if 'joindate' in empDict:
      empDict["joindate"] = dateutil.parser.parse(empDict["joindate"])
      return empDict


class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, datetime.date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)