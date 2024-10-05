contacts = {}

def parse_input(user_input):
    parts = user_input.lower().strip().split(' ')
    command = parts[0]
    args = parts[1:]
    return command, args

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added.")

def change_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        print(f"Contact {name} updated.")
    else:
        print(f"Contact {name} not found.")

def show_phone(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

def show_all_contacts():
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts available.")

def main():
    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)
        
        if command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            add_contact(args[0], args[1])
        elif command == "change" and len(args) == 2:
            change_contact(args[0], args[1])
        elif command == "phone" and len(args) == 1:
            show_phone(args[0])
        elif command == "show_all":
            show_all_contacts()
        elif command in ["exit", "close"]:
            print("Goodbye!")
            break
        else:
            print("Unknown command, please try again.")

if __name__ == "__main__":
    main()
