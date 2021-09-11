import requests
import json
from settings.loader import load_env
import os
from assets.query_assets import query_assets
from assets.query_asset_types import query_asset_types
from customers.query_customers import query_own_company

def run_samples():
    load_env()
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")
    print("Accessing " + str(server_url) + " with auth token " + str(token))
    company=query_own_company(server_url, token)
    company_pk=0
    if company is not None:
        company_pk=int(company['pk'])
        print("We are logged in as " + company['name'])
    query_asset_types(server_url, token)
    query_assets(server_url, token)

if __name__ == '__main__':
    run_samples()

