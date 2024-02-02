import csv

class Contacts:
    def __init__(self):
        with open('contacts.csv', 'r') as contact_list:
            csv_reader = csv.reader(contact_list)
            self._contacts = list(csv_reader)

    def add_contact(self, contact_dictionary):
        self._contacts.append(contact_dictionary)
        self._write_to_csv()

    def delete_contact(self, contact_name):
        for contact in self.contacts:
            if contact('Name') == contact_name:
                self._contacts.remove(contact)
                self._write_to_csv()
                break
    def _write_to_csv(self):
        with open('contacts.csv', )

    def
            
    


