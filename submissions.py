from client import Client
from credentials import credentials_dict
import requests



class Submissions:
    base_uri = 'https://client.id-pal.com/3.0.0/api/submission'

    def __init__(self, client):
        self.client = client

    def get_details(self,submission_id, content_disposition, base_uri):
        uri = base_uri + '/details'
        headers = {f'Authorization': f'Bearer {self.client.access_token}', 'Accept': 'application/json'}
        data = {'client_key': credentials_dict['client_key'],
                'access_key': credentials_dict['access_key'],
                'client_id': credentials_dict['client_id'],
                'refresh_token': credentials_dict['refresh_token']}
        r = requests.post(uri, headers=headers, data=data)

    def get_document(self, submission_id, content_disposition, base_uri):
        uri = base_uri + '/document'
        headers = {f'Authorization': f'Bearer {self.client.access_token}', 'Accept': 'application/json'}
        data = {'client_key': credentials_dict['client_key'],
                'access_key': credentials_dict['access_key'],
                'client_id': credentials_dict['client_id'],
                'refresh_token': credentials_dict['refresh_token']}
        r = requests.post(uri, headers=headers, data=data)






