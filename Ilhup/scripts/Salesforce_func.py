import pandas as pd
from simple_salesforce import Salesforce


def get_contact_by_NIL(sf, NIL):
    results = sf.query(f"SELECT ID, Name FROM Contact WHERE numero_invariant__c = '{NIL}'")
    # If results are found, return the first one
    if results['totalSize'] > 0:
        print('ok1')
        return results['records'][0]

    else:
        return None

def add_contact_to_campaign(sf, campaign_id, contact_id):
    # First, check if the contact is already in the campaign
    query = f"SELECT Id FROM CampaignMember WHERE CampaignId = '{campaign_id}' AND ContactId = '{contact_id}'"
    result = sf.query(query)

    if result['totalSize'] == 0:
        # The contact is not in the campaign, so add them
        sf.CampaignMember.create({'CampaignId': campaign_id, 'ContactId': contact_id})
        print('ok2')

def add_NIL_to_abs(sf, NIL):

    campaign_id = "701AZ0000009wR2YAI"
    contact = get_contact_by_NIL(sf, NIL)
    add_contact_to_campaign(sf, campaign_id, contact['Id'])
    print(f'{contact["Name"]} added')
def run():
    NIL = "400484040"
    abs_campaign_id = "701AZ0000009k7cYAA"
    add_NIL_to_abs(NIL)
