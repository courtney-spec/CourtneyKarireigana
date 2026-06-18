class ContactManager:
    def __init__(self):
        self.contacts = []

    # Task 1: Phone Validation
    def validate_phone(self, phone):
        if not phone.startswith("+256"):
            return False

        remaining_digits = phone[4:]

        if len(remaining_digits) != 9:
            return False

        if not remaining_digits.isdigit():
            return False

        return True

    # Task 1: Email Validation
    def validate_email(self, email):
        if email == "":
            return True
        return "@" in email and "." in email

    # Add Contact
    def add_contact(self, name, phone, email=""):
        if not self.validate_phone(phone):
            print("Error: Phone number must be in the format +256XXXXXXXXX.")
            return

        if not self.validate_email(email):
            print("Error: Invalid email format.")
            return

        self.contacts.append((name, phone, email))
        print("Contact added successfully!")

    # View Contact
    def view_contact(self, name):
        for contact in self.contacts:
            if contact[0].lower() == name.lower():
                print("\nContact Found")
                print(f"Name: {contact[0]}")
                print(f"Phone: {contact[1]}")
                print(f"Email: {contact[2]}")
                return

        print("Contact not found.")

    # Update Contact
    def update_contact(self, name, new_phone, new_email=""):
        if not self.validate_phone(new_phone):
            print("Error: Phone number must be in the format +256XXXXXXXXX.")
            return

        if not self.validate_email(new_email):
            print("Error: Invalid email format.")
            return

        for i, contact in enumerate(self.contacts):
            if contact[0].lower() == name.lower():
                self.contacts[i] = (name, new_phone, new_email)
                print("Contact updated successfully!")
                return

        print("Contact not found.")

    # Delete Contact
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact[0].lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return

        print("Contact not found.")

    # Task 2: Advanced Search
    def search_contacts(self, keyword):
        results = []

        for contact in self.contacts:
            if (keyword.lower() in contact[0].lower() or
                    keyword.lower() in contact[1].lower() or
                    keyword.lower() in contact[2].lower()):
                results.append(contact)

        if len(results) == 0:
            print("No matching contacts found.")
        else:
            print("\n=== Search Results ===")
            for i, contact in enumerate(results, start=1):
                print(f"{i}. Name: {contact[0]}")
                print(f"   Phone: {contact[1]}")
                print(f"   Email: {contact[2]}")
                print("-" * 30)

    # List All Contacts
    def list_all_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts available.")
            return

        print("\n=== All Contacts ===")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. Name: {contact[0]}")
            print(f"   Phone: {contact[1]}")
            print(f"   Email: {contact[2]}")
            print("-" * 30)


def main():
    manager = ContactManager()

    while True:
        print("\n=== Contact Manager ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email (optional): ")
            manager.add_contact(name, phone, email)
        elif choice == "2":
            name = input("Enter name to view: ")
            manager.view_contact(name)
        elif choice == "3":
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email (optional): ")
            manager.update_contact(name, new_phone, new_email)
        elif choice == "4":
            name = input("Enter name to delete: ")
            manager.delete_contact(name)
        elif choice == "5":
            keyword = input("Enter keyword to search: ")
            manager.search_contacts(keyword)
        elif choice == "6":
            manager.list_all_contacts()
        elif choice == "7":
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()