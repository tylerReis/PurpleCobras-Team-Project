import csv
import os 

class Contacts:
    def __init__(self):
#Creates a CSV File
        self._csv_filename = 'contacts.csv'
        self._initialize_csv()

        with open('contacts.csv', 'r') as contact_list:
            csv_reader = csv.DictReader(contact_list)
            self._contacts = list(csv_reader)
    def _initialize_csv(self):
        if not os.path.isfile(self._csv_filename):
            with open(self._csv_filename,'w', newline = '') as contact_list:
                csv_writer = csv.writer(contact_list)
                csv_writer.writerow(['Name', 'Phone'])
#Method to add contacts
    def add_contact(self):
        print("Enter contact details:")
        name = input("Name:")
        phone = input("Phone Number:")
        contact_dict = {'Name': name, 'Phone': phone}
        self._contacts.append(contact_dict)
        self._write_to_csv()
        print('Contact added successfully.')
#Method to Delete Contacts
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
        with open('contacts.csv', 'w', newline='') as contact_list:
            csv_writer = csv.DictWriter(contact_list, fieldnames=['Name', 'Phone'])
            csv_writer.writeheader()

            for contact in self._contacts:
                csv_writer.writerow(contact)


        

    #This is Tyler's comment

contact_manager = Contacts()

contact_manager.add_contact()
contact_manager.add_contact()
contact_manager.add_contact()


    
contact_manager.display_contacts()


            
    


