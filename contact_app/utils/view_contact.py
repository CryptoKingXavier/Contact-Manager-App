from csv import reader

def show_contacts() -> None:
    # Info: To display all contacts
    contacts_list: list[list[str]] = list()

    with open('contacts.csv', 'r') as phonebook:
        csvreader = reader(phonebook)
        for row in csvreader:
            contacts_list.append(row)
        phonebook.close()
        contacts_list.sort()
    
    return contacts_list

def show_contact(contact_name: str) -> None:
    # Info: To display a single contact
    contacts_list: list[list[str]] = list()

    with open('contacts.csv', 'r') as phonebook:
        csvreader = reader(phonebook)
        for row in csvreader:
            contacts_list.append(row)
        phonebook.close()

        for contact in contacts_list:
            if contact_name.strip() in contact:
                return contact
