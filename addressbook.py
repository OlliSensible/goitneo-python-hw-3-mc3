from collections import defaultdict
from datetime import datetime, timedelta
from record import Record
import pickle


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, name, phone, birthday=None):
        if name in self.data:
            self.data[name].add_phone(phone)
            self.data[name].add_birthday(birthday)
        else:
            self.data[name] = Record(name, phone, birthday)

    def count_records(self):
        return len(self.data)

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise KeyError("Name not found")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Name not found")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    def load_from_file(self, filename):
        with open(filename, 'rb') as file:
            self.data = pickle.load(file)

    def get_birthdays_per_week(self):
        today = datetime.now().date()
        next_week = today + timedelta(days=7)
        upcoming_birthdays = {day: [] for day in range(7)}

        for name, record in self.data.items():
            if record.birthday:
                bday = datetime.strptime(record.birthday.value, '%d.%m.%Y').date()
                if today <= bday < next_week:
                    day = (bday - today).days
                    if day < 0:
                        day += 365
                    upcoming_birthdays[day].append((name, bday))

        return upcoming_birthdays

def handle_all_birthdays(address_book):
    birthdays_by_date = defaultdict(list)

    today = datetime.now().date()

    for name, record in address_book.data.items():
        if record.birthday:
            bday = datetime.strptime(record.birthday.value, '%d.%m.%Y').date()

            for i in range(7):
                future_date = today + timedelta(days=i)
                if bday.day == future_date.day and bday.month == future_date.month:
                    birthdays_by_date[future_date].append(name)

    while birthdays_by_date:
        upcoming_dates = [today + timedelta(days=day_offset) for day_offset in range(7)]

        for day in upcoming_dates:
            day_of_week = day.strftime("%A")
            names = birthdays_by_date.get(day, [])
            if names:
                names = [name.capitalize() for name in names]
                if day_of_week == "Saturday":
                    # Зсуваємо вивід на понеділок
                    next_monday = today + timedelta(days=7 - today.weekday())
                    day_of_week = "Monday"
                print(f"{day_of_week}: {', '.join(names)}")

            if day in birthdays_by_date:
                del birthdays_by_date[day]
