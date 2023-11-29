from csv import reader, writer
from typing import Mapping

def update_contact(contact_name: str, new_name: str, new_number: str) -> None:
    # Info: To update a contact
    contacts_list: list[list[str]] = list()
    contacts_dict: Mapping[str, str] | None = None

    with open('contacts.csv', 'r') as phonebook:
        csvreader = reader(phonebook)
        for row in csvreader:
            contacts_list.append(row)
        phonebook.close()
        contacts_list.sort()
        contacts_dict = dict(contacts_list)

    if contact_name.strip() not in contacts_dict.keys():
        print("Contact Doesn't Exist!")
        return

    for contact in contacts_list:
        if contact_name in contact:
            contact[0] = new_name.strip()
    
    for contact in contacts_list:
        if contact_name in contact:
            contact[1] = new_number.strip()

    contacts_list.sort()

    with open('contacts.csv', 'w', newline='') as phonebook: 
        writer(phonebook).writerows(contacts_list)
        phonebook.close()
