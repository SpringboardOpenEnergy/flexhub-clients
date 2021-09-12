import requests
import json
from settings.loader import load_env
import os

def query_asset_types(server_url, token):

    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/assets/assettype/'
    #print(json.dumps(qry, indent=2))
    result = requests.get(url,  headers=headers)
    print(result)
    print(json.dumps(result.json(), indent=2))


if __name__ == '__main__':
    load_env()
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")
    query_asset_types(server_url, token)