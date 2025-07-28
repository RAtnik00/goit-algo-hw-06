from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be at least 10 digits long and contain only numbers.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {';'.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return f"Phone {phone} removed."
        return f"Phone {phone} not found."
    
    def edit_phone(self, old_phone: str, new_phone: str):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return f"Phone {old_phone} changed to {new_phone}."
        return f"Phone {old_phone} not found."

class AddressBook(UserDict):
    pass

r = Record("John")
r.add_phone("1234567890")
print(r.edit_phone("1234567890", "1112223333"))  # має змінити
print(r.edit_phone("9999999999", "0000000000"))  # має кинути ValueError

