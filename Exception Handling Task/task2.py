import re

class EmptyFieldError(Exception):
    pass

class InvalidPhoneError(Exception):
    pass

class DuplicateContactError(Exception):
    pass

contacts = {}  # name: phone

def add_or_edit_contact():
    try:
        name = input("Enter name: ").strip()
        if not name:
            raise EmptyFieldError("Name cannot be empty.")
        if name in contacts:
            print(f"Contact '{name}' exists. Updating phone.")
        phone = input("Enter phone (10 digits): ").strip()
        if not phone:
            raise EmptyFieldError("Phone cannot be empty.")
        if not re.match(r'^\d{10}$', phone):
            raise InvalidPhoneError("Phone must be exactly 10 digits.")
        contacts[name] = phone
        print(f"Contact '{name}' saved with {phone}.")
    except EmptyFieldError as e:
        print(f"Error: {e}")
    except InvalidPhoneError as e:
        print(f"Error: {e}")

def search_contact():
    try:
        name = input("Enter name to search: ").strip()
        if not name:
            raise EmptyFieldError("Name cannot be empty.")
        phone = contacts[name]
        print(f"{name}: {phone}")
    except KeyError:
        print("Contact not found.")
    except EmptyFieldError as e:
        print(f"Error: {e}")

def delete_contact():
    try:
        name = input("Enter name to delete: ").strip()
        if not name:
            raise EmptyFieldError("Name cannot be empty.")
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            raise KeyError("Contact not found.")
    except KeyError as e:
        print(f"Error: {e}")
    except EmptyFieldError as e:
        print(f"Error: {e}")

def list_contacts():
    if not contacts:
        print("No contacts.")
    else:
        for n, p in contacts.items():
            print(f"{n}: {p}")

while True:
    print("\n1. Add/Edit  2. Search  3. Delete  4. List  5. Exit")
    choice = input("Choose: ").strip()
    if choice == '1':
        add_or_edit_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        
        delete_contact()
    elif choice == '4':
        list_contacts()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
