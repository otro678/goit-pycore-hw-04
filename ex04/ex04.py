def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(contacts, name, phone):
    try:
        if name in contacts:
            overwrite = input(f"Contact '{name}' already exists. Do you want to overwrite? (y/n): ").strip().lower()
            if overwrite == "n":
                return "Operation canceled"
            if overwrite != "y":
                return "Unknown answer, returning to the main menu"

        contacts[name] = int(phone)
    except Exception as e:
        return f"There was an error adding contact. Error: {e}"
    return "Contact added"

def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated"
    else:
        return "Contact not found"

def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command in ["hello", "hi", "wassup"]:
            print("How can I help you? Possible commands are: \n- add [name] [phone]\n- change or update [name] [phone]\n- phone or show [name]\n- all")

        elif command == "add":
            if len(args) == 2:
                name, phone = args
                print(add_contact(contacts, name, phone))
            else:
                print("Invalid command usage, should be: add [name] [phone]")

        elif command in ["change", "update"]:
            if len(args) == 2:
                name, phone = args
                print(change_contact(contacts, name, phone))
            else:
                print("Invalid command usage, should be: change [name] [phone]")

        elif command in ["phone", "show"]:
            if len(args) == 1:
                name = args[0]
                print(show_phone(contacts, name))
            else:
                print("Invalid command usage, should be: phone [name]")

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command")

if __name__ == "__main__":
    main()