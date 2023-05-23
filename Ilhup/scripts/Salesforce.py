import pandas as pd
from simple_salesforce import Salesforce


# Salesforce Login
Contact_ID = "003AZ000002hejbYAA"
security_token = "tp6dNCvSN469M2Km3vGlwpmi"
username = "guillaume.nguyen-thi@reseauilhup.com"
pw = "Lor4hecha@@"

#sf = Salesforce(instance_url='https://ilhup.my.salesforce.com/', session_id='')
sf = Salesforce(username=username, password=pw, security_token=security_token)

contact = sf.Contact.get(Contact_ID)
print(f'\n{contact}')
# Query Salesforce for a contact by name
results = sf.query("SELECT Id, Name FROM Contact WHERE Name = '1 Test'")

# If results are found, access the first one
if results['totalSize'] > 0:
    contact = results['records'][0]
    print(contact['Id'])
else:
    print('Contact not found')

