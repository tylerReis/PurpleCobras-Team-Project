import csv

class Contacts:
    def __init__(self):
        with open('contacts.csv', 'r') as contact_list:
            csv_reader = csv.reader(contact_list)
            self._contacts = list(csv_reader)

    def add_contact(self, contact_dictionary):
        with open('contacts.csv', 'w') as contact_list:
            contact_list.write(contactDictionary)
            contact_list.write('\n')

    def delete_contact(self, contact_Name):

    def
            
    


