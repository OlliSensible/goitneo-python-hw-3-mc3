from field import Name, Phone, Birthday

class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = Name(name)
        self.phones = [Phone(phone)]
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        if Phone.is_valid(phone):
            self.phones.append(Phone(phone))
        else:
            raise ValueError("Invalid phone number")

    def add_birthday(self, birthday):
        if not birthday:
            return
        if Birthday.is_valid(birthday):
            self.birthday = Birthday(birthday)
        else:
            raise ValueError("Invalid birthday date")

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break
        else:
            raise KeyError("Phone number not found")

    def edit_phone(self, old_phone, new_phone):
        if not Phone.is_valid(new_phone):
            raise ValueError("Invalid new phone number")

        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break
        else:
            raise KeyError("Phone number not found")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        else:
            raise KeyError("Phone number not found")
