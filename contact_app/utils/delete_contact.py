from csv import reader, writer
from typing import Mapping

def delete_contact(contact_name: str) -> None:
    contacts_list: list[list[str]] = list()
    contacts_dict: Mapping[str, str] | None = None

    with open('contacts.csv', 'r') as phonebook:
        csvreader = reader(phonebook)
        for row in csvreader:
            contacts_list.append(row)
        phonebook.close()
        contacts_list.sort()
        contacts_dict = dict(contacts_list)

    if contacts_dict.__len__() != 0:
        try:
            del contacts_dict[contact_name.strip()]
            contacts_list: list[list[str]] = list([name, number] for (name, number) in zip(contacts_dict.keys(), contacts_dict.values()))
            contacts_list.sort()

            with open('contacts.csv', 'w', newline='') as phonebook:
                writer(phonebook).writerows(contacts_list)
                phonebook.close()

        except KeyError:
            pass

delete_contact('Ahmed')