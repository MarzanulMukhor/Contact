import csv

CONTACTSFILE = "contacts.csv"

#Load contacts from a file into a list
def load_contacts():

    contacts = []
    try:
        with open(CONTACTSFILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        pass
    return contacts

#Save contacts to a file.
def save_contacts(contacts):

    with open(CONTACTSFILE, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["Name", "Email", "Phone", "Address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

#Display all contacts
def display_contacts(contacts):

    if not contacts:
        print("\nNo contacts to display.\n")
        return
    print("\n--- Contacts List ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}:")
        for key, value in contact.items():
            print(f"  {key}: {value}")
    print()

#Add a contact which can't be duplicate
def add_contact(contacts):

    print("\nAdd Contact --")
    name = input(str("Enter Name: ")).strip()
    email = input(str("Enter Email: ")).strip()
    phone = input("Enter Phone Number: ").strip()
    address = input(str("Enter Address: ")).strip()


    if any(contact['Phone'] == phone for contact in contacts):
        print("\nThis contact number already exists.\n")
        return contacts

    # Add the new contact
    new_contact = {"Name": name, "Email": email, "Phone": phone, "Address": address}
    contacts.append(new_contact)
    save_contacts(contacts)
    print("\nContact added successfully and saved to file!")
    return contacts

#Remove a contact
def remove_contact(contacts):

    print("\nRemove Contact ")
    name_to_remove = input("Enter the name of the contact to remove: ").strip()
    for contact in contacts:
        if contact["Name"].lower() == name_to_remove.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"\nContact '{name_to_remove}' removed successfully!")
            return contacts
    print(f"\nContact '{name_to_remove}' not found.")
    return contacts

#Contact Management System
def main():

    contacts = load_contacts()
    while True:
        print("\nWelcome to our Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            contacts = add_contact(contacts)
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            contacts = remove_contact(contacts)
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
