from datetime import datetime, timedelta

def input_error(func):
    def wrapper(args, book):
        try:
            return func(args, book)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return wrapper

class Birthday:
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        if len(phone) != 10 or not phone.isdigit():
            raise ValueError("Phone number must be 10 digits.")
        self.phones.append(phone)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

class AddressBook:
    def __init__(self):
        self.records = {}

    def add_record(self, record):
        self.records[record.name.value] = record

    def find(self, name):
        return self.records.get(name)

    def get_upcoming_birthdays(self):
        upcoming = []
        today = datetime.today()
        for record in self.records.values():
            if record.birthday:
                days_diff = (record.birthday.value - today).days
                if 0 <= days_diff <= 7:
                    upcoming.append({"name": record.name.value, "birthday": str(record.birthday)})
        return upcoming

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.add_birthday(birthday)
    return f"Birthday for {name} added."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if not record or not record.birthday:
        return "Birthday not found."
    return f"{name}'s birthday is {record.birthday}."

@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    return "\n".join([f"{entry['name']} - {entry['birthday']}" for entry in upcoming])

@input_error
def add_contact(args, book):
    name, phone = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
    record.add_phone(phone)
    return f"Contact {name} added/updated."

@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    if old_phone not in record.phones:
        return "Old phone number not found."
    record.phones.remove(old_phone)
    record.add_phone(new_phone)
    return f"Phone number for {name} updated."

@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if not record or not record.phones:
        return "Phone number not found."
    return f"{name}'s phone numbers: {', '.join(record.phones)}"

@input_error
def show_all_contacts(args, book):
    if not book.records:
        return "No contacts found."
    return "\n".join([f"{record.name.value} - {', '.join(record.phones)}" for record in book.records.values()])

def parse_input(user_input):
    return user_input.split()

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all_contacts(args, book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
