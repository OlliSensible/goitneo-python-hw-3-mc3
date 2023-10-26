from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self, number):
        if not self.is_valid(number):
            raise ValueError("Invalid phone number")
        super().__init__(number)

    @staticmethod
    def is_valid(number):
        return len(number) == 10 and number.isdigit()


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Birthday(Field):
    def __init__(self, date):
        if not self.is_valid(date):
            raise ValueError("Invalid birthday date")
        super().__init__(date)

    @staticmethod
    def is_valid(date):
        try:
            datetime.strptime(date, '%d.%m.%Y')
            return True
        except ValueError:
            return False
