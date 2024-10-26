import re
from collections import UserDict


# Validation for correct number made with own exception in class Phone
#
# all the classes has their methods with realisation and all works fine
#
# mainly prints copied from the task, added a couple other for better visualisation
# of result


class PhoneNumberDoesNotExist(Exception):
    pass


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        pattern = re.compile(r"\d{10}")
        if re.search(pattern, phone):
            super().__init__(phone)
        else:
            raise PhoneNumberDoesNotExist


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except PhoneNumberDoesNotExist:
            pass

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value

    def remove_phone(self, phone):
        i = 0
        for p in self.phones:
            if p.value == phone:
                self.phones.pop(i)
            i += 1

    def edit_phone(self, old, new):
        for p in self.phones:
            p.value = new if p.value == old else p.value

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[str(record.name)] = record

    def find(self, name):
        return self.data[name]

    def delete(self, name):
        self.data.pop(name, None)


# test


def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John та Додавання запису John до адресної книги
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_phone("7777777__7")
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Пошук конкретного телефону у записі John
    john = book.find("John")
    found_phone = john.find_phone("5555555555")
    print(f"\n{john.name}: {found_phone}")

    # Знаходження та редагування телефону для John
    john = book.find("John")
    print(f"\nEDIT phone before and after:\n{john}")
    john.edit_phone("1234567890", "1112223333")
    print(f"{john}")

    # Видалення телефону у у записі John
    print(f"\nREMOVE phone before and after:\n{john}")
    john.remove_phone("1112223333")
    print(f"{john}")


if __name__ == "__main__":
    main()
