import requests
import json
from settings.loader import load_env
import os
from customers.query_customers import query_own_company, query_company_list

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
                "asset_type": server_url + "/api/assets/assettype/" + str(asset_type_pk) + "/",
                "grid_connection": server_url + "/api/customers/company/"+ str(grid_comp_pk) + "/",
                "power_supplier": None,
                "asset_owner": server_url+ "/api/customers/company/" + str(asset_manager_pk) + "/",
                "asset_manager": server_url + "/api/customers/company/" + str(asset_manager_pk) + "/",
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

#Specify existing KEY (PK) see asset list for mapping form asset_id. Must be allowed to manage this asset
def update_asset(server_url, token,
                   extern_id,
                   description,
                   asset_type_pk,
                   asset_manager_pk,
                   grid_comp_pk,
                   meter_id, pk):
    new_asset= {
                "extern_asset_id": extern_id,
                "description": description,
                "asset_type": server_url + "/api/assets/assettype/" + str(asset_type_pk) + "/",
                "grid_connection": server_url + "/api/customers/company/"+ str(grid_comp_pk) + "/",
                "power_supplier": None,
                "asset_owner": server_url+ "/api/customers/company/" + str(asset_manager_pk) + "/",
                "asset_manager": server_url + "/api/customers/company/" + str(asset_manager_pk) + "/",
                "meter_id": meter_id,
                "sub_meter_id": None,
                "latitude": "0",
                "longitude": "0",
                "is_active": True
            }
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/assets/asset/' + str(pk) + '/'
    result = requests.patch(url, json=new_asset, headers=headers)
    print(result, json.dumps(result.json(), indent=2))

if __name__ == '__main__':
    load_env()
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")
    my_fsp_pk=0
    company = query_own_company(server_url, token)
    if company is not None:
        my_fsp_pk=int(company['pk'])
        print("We are logged in as " + company['name'])
    dso_list=query_company_list(server_url, token, "DSO")
    grid_comp_pk=0 if len(dso_list)==0 else dso_list[0]['pk'] #Use first DSO in list as sample grid compnay
    print("Registering asset against grid company " + str(grid_comp_pk))
    asset_type_pk=1 # Demand respones (or pick one from the list above)
    extern_asset_id="623342342342342" # WHat ever extern ID to lookup later on
    description="My electric asset # 423"
    meter_id="74545928329372384"
    #register_asset(server_url, token,extern_asset_id,description,asset_type_pk,my_fsp_pk, grid_comp_pk, meter_id)
    #update_asset(server_url, token, extern_asset_id, description, asset_type_pk, my_fsp_pk, grid_comp_pk, meter_id, 120)