import csv

class Contacts:
    def __init__(self):
        with open('contacts.csv', 'r') as contact_list:
            csv_reader = csv.reader(contact_list)
            self._contacts = list(csv_reader)

    def add_contact(self, contact):
        with open('contacts.csv', 'w') as contact_list:
            
    


# import json


# class SatData: 
#     def __init__(self, data_file):
#          with open('sat.json', 'r') as sat_file:
#             self._sat_data = json.load(sat_file)

#     def save_as_csv(self, DBN_list):
#         with open("output.csv", "w") as outfile:
#             for school in self._sat_data['data']:
#                 for dbn in DBN_list:
#                     if dbn == school[8]:
                    
#                         for index in range(8 ,13):
#                             outfile.write(school[index] + ",")
#                         outfile.write('\n')


# sd = SatData('sat.json')
# dbns = ["02M303", "02M294", "01M450", "02M418"]
# sd.save_as_csv(dbns)