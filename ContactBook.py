class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for index, contact in enumerate(self.contacts):
                print(f"{index + 1}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if results:
            print("Search Results:")
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("No matching contacts found.")

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f"Contact {name} updated successfully!")
                return
        print(f"Contact {name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully!")
                return
        print(f"Contact {name} not found.")

    def user_interface(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Select an option (1-6): ")

            if choice == '1':
                name = input("Enter Name: ")
                phone = input("Enter Phone Number: ")
                email = input("Enter Email: ")
                address = input("Enter Address: ")
                self.add_contact(name, phone, email, address)

            elif choice == '2':
                self.view_contacts()

            elif choice == '3':
                search_term = input("Enter Name or Phone Number to search: ")
                self.search_contact(search_term)

            elif choice == '4':
                name = input("Enter the Name of the contact to update: ")
                print("Leave blank if no change is required.")
                new_phone = input("Enter new Phone Number: ")
                new_email = input("Enter new Email: ")
                new_address = input("Enter new Address: ")
                self.update_contact(name, new_phone, new_email, new_address)

            elif choice == '5':
                name = input("Enter the Name of the contact to delete: ")
                self.delete_contact(name)

            elif choice == '6':
                print("Exiting Contact Book. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

# Instantiate the ContactBook and start the user interface
contact_book = ContactBook()
contact_book.user_interface()