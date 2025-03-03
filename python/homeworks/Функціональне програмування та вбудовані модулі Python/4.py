def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide the arguments."
    return inner

class Bot:
    def __init__(self):
        self.contacts = {}

    @input_error
    def add_contact(self, args):
        name, phone = args
        self.contacts[name] = phone
        return "Contact added."

    @input_error
    def show_phone(self, args):
        name = args[0]
        return f"{name}: {self.contacts[name]}"

    @input_error
    def show_all_contacts(self, args):
        if not self.contacts:
            return "No contacts available."
        return "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])

    def handle_command(self, command):
        args = command.split()
        if not args:
            return "Enter a command:"

        command = args[0].lower()
        if command == "add" and len(args) > 1:
            return self.add_contact(args[1:])
        elif command == "phone" and len(args) > 1:
            return self.show_phone(args[1:])
        elif command == "all":
            return self.show_all_contacts(args)
        else:
            return "Unknown command or missing arguments."


def main():
    bot = Bot()
    while True:
        command = input("Enter a command: ")
        response = bot.handle_command(command)
        print(response)

if __name__ == "__main__":
    main()
