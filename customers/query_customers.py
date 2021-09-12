import requests
import json
from settings.loader import load_env
import os

def query_company_list(server_url, token, role_type):
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/customers/query_companies_with_role/'
    #print(json.dumps(qry, indent=2))
    query= {
                "role": role_type
    }
    result = requests.post(url, json=query, headers=headers)
    print(result)
    print(json.dumps(result.json(), indent=2))
    return result.json()['companies']

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