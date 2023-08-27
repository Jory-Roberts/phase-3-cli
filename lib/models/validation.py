import re
from datetime import datetime


class Validation:
    @staticmethod
    def email(email):
        pattern = re.compile("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
        return re.fullmatch(pattern, email) is not None

    @staticmethod
    def phone_number(phone_number):
        pattern = re.compile("\d{3}-\d{3}-\d{4}$")
        return re.fullmatch(pattern, phone_number) is not None

    @staticmethod
    def date(input_date):
        try:
            datetime.strptime(input_date, "%Y-%m-%d").date()
            return True
        except ValueError:
            return False
