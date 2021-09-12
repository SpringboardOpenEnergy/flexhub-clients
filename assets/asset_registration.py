import requests
import json
from settings.loader import load_env
import os

def register_asset(server_url, token,
                   extern_id,
                   description,
                   asset_type_pk,
                   asset_manager_pk,
                   grid_comp_pk,
                   meter_id):
    new_asset= {
                "extern_asset_id": extern_id,
                "description": description,
                "asset_type": "http://127.0.0.1:8000/api/assets/assettype/" + str(asset_type_pk) + "/",
                "grid_connection": "http://127.0.0.1:8000/api/customers/company/"+ str(grid_comp_pk) + "/",
                "power_supplier": None,
                "asset_owner": "http://127.0.0.1:8000/api/customers/company/" + str(asset_manager_pk) + "/",
                "asset_manager": "http://127.0.0.1:8000/api/customers/company/" + str(asset_manager_pk) + "/",
                "meter_id": meter_id,
                "sub_meter_id": None,
                "latitude": "0",
                "longitude": "0",
                "is_active": True
            }
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/assets/asset/'
    result = requests.post(url, json=new_asset, headers=headers)
    print(result, json.dumps(result.json(), indent=2))