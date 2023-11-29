from csv import writer, reader
from typing import Mapping

def add_contact(contact_name: str, contact_number: str) -> None:
    contacts_list: list[list[str]] = list()
    contacts_dict: Mapping[str, str] | None = None

    with open('contacts.csv', 'r') as phonebook:
        csvreader = reader(phonebook)
        for row in csvreader:
            contacts_list.append(row)
        phonebook.close()
        contacts_list.sort()
        contacts_dict = dict(contacts_list)

    if contact_name not in contacts_dict.keys() and contact_number not in contacts_dict.values():
        contacts_list.append([contact_name.strip(), contact_number.strip()])
        contacts_list.sort()

    with open('contacts.csv', 'w', newline='') as phonebook:
        writer(phonebook).writerows(contacts_list)
        phonebook.close()
