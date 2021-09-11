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
def query_customer_list(server_url, token):
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/customers/query_companies_by_type/'
    #print(json.dumps(qry, indent=2))
    result = requests.get(url,  headers=headers)
    print(result)
    print(json.dumps(result.json(), indent=2))

def query_own_company(server_url, token):
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/customers/company/'
    result = requests.get(url,  headers=headers)
    print(result)
    print(json.dumps(result.json(), indent=2))
    if len(result.json())==0:
        return None
    return result.json()[0]  # For simplicity in sample, select first company - most common case is only 1

if __name__ == '__main__':
    load_env()
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")
    query_own_company(server_url, token)