import json
import os

import requests

from settings.loader import load_env


def query_assets(server_url, token):
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/assets/asset/'
    result = requests.get(url,  headers=headers)
    print(result)
    print(json.dumps(result.json(), indent=2))
    return result.json()


if __name__ == '__main__':
    load_env()
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")
    query_assets(server_url, token)