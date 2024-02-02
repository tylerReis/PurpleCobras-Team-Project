import csv
import os 

class Contacts:
    def __init__(self):
#Creates a CSV File
        self._csv_filename = 'contacts.csv'
        self._initialize_csv()

        with open('contacts.csv', 'r') as contact_list:
            csv_reader = csv.reader(contact_list)
            self._contacts = list(csv_reader)

    def add_contact(self):
        print("Enter contact details:")
        name = input("Name:")
        phone = input("Phone Number:")
        contact_dict = {'Name': name, 'Phone': phone}
        self._contacts.append(contact_dict)
        self._write_to_csv()
        print('Contact added successfully.')

    def delete_contact(self):
        print("Enter contact to be deleted:")
        contact_name = input('Name: ')
        for contact in self._contacts:
            if contact['Name'] == contact_name:
                self._contacts.remove(contact)
                self._write_to_csv()
                print('contact delted successfully')
                break
    def display_contacts(self):
        if self._contacts:
            print("\nContacts:")
            for contact in self._contacts:
                print(contact)
        else:
            print("\nNo contacts available.")

    def _write_to_csv(self):
        with open('contacts.csv', 'w', newline= '') as contact_list:
            csv_writer = csv.writer(contact_list)
            csv_writer.writerows([contact.values() for contact in self._contacts])

    #This is Tyler's comment

contact_manager = Contacts()

contact_manager.add_contact()         
contact_manager.add_contact()
contact_manager.add_contact()
contact_manager.add_contact()
contact_manager.add_contact()

            
    


