import requests, json
from credentials import credentials_dict




def refresh_token(refresh_token):
    def wrapper():
        uri = credentials_dict['base_uri'] + 'getAccessToken'
        headers = {f'Authorization': f'Bearer {refresh_token}', 'Accept': 'application/json'}
        data = {'client_key' : credentials_dict['client_key'],
                'access_key' : credentials_dict['access_key'],
                'client_id' : credentials_dict['client_id'],
                'refresh_token' : credentials_dict['refresh_token']}

        try:
            r = requests.post(uri,headers=headers,data=data)
        except:
            print("test")


