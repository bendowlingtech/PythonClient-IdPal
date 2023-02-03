from credentials import credentials_dict
import requests

class Client:

    def __init__(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = access_token



    def refresh_token(self, func):
        def wrapper():

            try:
                func()


            except requests.exceptions.HTTPError:
                uri = credentials_dict['base_uri'] + 'getAccessToken'
                headers = {f'Authorization': f'Bearer {self.refresh_token}', 'Accept': 'application/json'}
                data = {'client_key': credentials_dict['client_key'],
                        'access_key': credentials_dict['access_key'],
                        'client_id': credentials_dict['client_id'],
                        'refresh_token': credentials_dict['refresh_token']}
                r = requests.post(uri, headers=headers, data=data)
                print(r.text)





            #self.access_token = r['placeholder']
            #self.refresh_token = r['placeholder']



