def add_or_update_contact(contacts, contact_number, contact_name):
    if contact_number in contacts:
        print("Contact number already exists.")
        print("1. Update contact details")
        print("2. Do not update")
        while True:
            try:
                choice = int(input("Enter your choice (1/2): "))
                if choice == 1:
                    contacts[contact_number]['name'] = contact_name
                    print("Contact details updated.")
                    break
                elif choice == 2:
                    print("Contact details not updated.")
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        contacts[contact_number] = {'name': contact_name}
        print("Contact details added.")


if __name__ == '__main__':
    contacts = {
        '1234567890': {'name': 'aayush'},
        '0987654321': {'name': 'prankur'},
    }
    add_or_update_contact(contacts, '1234567890', 'aayush')
    add_or_update_contact(contacts, '9876543210', 'prankur')
    add_or_update_contact(contacts, '1234567890', 'aayush')
