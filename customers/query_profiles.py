import requests
import json
from settings.loader import load_env
import os


def query_current_profile(server_url, token):
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/customers/profile/'
    result = requests.get(url,  headers=headers)
    print(result)
    print(json.dumps(result.json(), indent=2))
    if len(result.json())==0:
        return None
    return result.json()  # For simplicity in sample, select first company - most common case is only 1

if __name__ == '__main__':
    load_env()
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")
    query_current_profile (server_url, token)