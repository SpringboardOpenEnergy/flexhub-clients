import requests
import json
from settings.loader import load_env
import os
qry={
    "assets":["fedd1ef3-c877-4f63-a3a0-f256d957df84"],
    "from_datetime":"2020-10-07 00:00:00",
    "to_datetime":"2020-10-23 00:00:00",
    "resolution_minutes":60
}
def query_assets(server_url, token):
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/assets/asset/'
    #print(json.dumps(qry, indent=2))
    result = requests.get(url,  headers=headers)
    print(result)
    print(json.dumps(result.json(), indent=2))


if __name__ == '__main__':
    load_env()
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")
    query_assets(server_url, token)