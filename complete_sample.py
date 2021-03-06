import os
from assets.query_assets import query_assets
from customers.query_customers import query_own_company, query_company_list
from readings.ingest_assetmeter_readings import ingest_assetlevel_readings
from settings.loader import load_env


def run_samples():
    load_env()
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")  # http://test.flexhub.no for test system
    print("Accessing " + str(server_url) + " with auth token " + str(token))
    company=query_own_company(server_url, token)
    my_fsp_pk=0
    if company is not None:
        my_fsp_pk=int(company['pk'])
        print("We are logged in as " + company['name'])
    query_asset_types(server_url, token)
    assetlist=query_assets(server_url, token)

    dso_list=query_company_list(server_url, token, "DSO")
    grid_comp_pk=0 if len(dso_list)==0 else dso_list[0]['pk'] #Use first DSO in list as sample grid compnay
    print("Registering asset against grid company " + str(grid_comp_pk))
    asset_type_pk=1 # Demand respones (or pick one from the list above)
    extern_asset_id="123342342342342" # WHat ever extern ID to lookup later on
    description="My super asset # 122"
    meter_id="79928329372384"

    # The asset is assigned asset_id by server (used to refer to when registering meter readings
    # Use own extern_asset_id to map to own data as a way of linking to correct asset_id

    # Uncomment to send registration
    #register_asset(server_url, token,extern_asset_id,description,asset_type_pk,my_fsp_pk, grid_comp_pk, meter_id)

    #Sample reading registration.
    if len(assetlist)>0:
        firstasset=assetlist[0]
        print("Ingesting sample readings for " + firstasset['asset_id'])
        ingest_assetlevel_readings(server_url, token, firstasset['asset_id'])
if __name__ == '__main__':
    run_samples()

