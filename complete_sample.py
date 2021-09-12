import requests
import json
from settings.loader import load_env
import os
from assets.query_assets import query_assets
from assets.query_asset_types import query_asset_types
from customers.query_customers import query_own_company
from assets.asset_registration import register_asset
def run_samples():
    load_env()
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")
    print("Accessing " + str(server_url) + " with auth token " + str(token))
    company=query_own_company(server_url, token)
    my_fsp_pk=0
    if company is not None:
        my_fsp_pk=int(company['pk'])
        print("We are logged in as " + company['name'])
    query_asset_types(server_url, token)
    query_assets(server_url, token)
    asset_type_pk=1 # Demand respones (or pick one from the list above)
    grid_comp_pk=4 # Sample DSO
    extern_asset_id="abcdef" # WHat ever extern ID to lookup later on
    description="My super asset # 122"
    meter_id="79928329372384"
    register_asset(server_url, token,extern_asset_id,description,asset_type_pk,my_fsp_pk, grid_comp_pk, meter_id)

if __name__ == '__main__':
    run_samples()

