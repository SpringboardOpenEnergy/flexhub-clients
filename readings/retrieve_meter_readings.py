import requests
import json
from settings.loader import load_env
import os


def retrieve_readings_for_asset(server_url, token, asset_id):
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/assetdata/query_meterreadings/'
    qry_payload = {
        "assets": [asset_id],
        "from_datetime": "2021-05-07 00:00:00",
        "to_datetime": "2021-06-23 00:00:00",
        "resolution_minutes": 60
    }

    print(json.dumps(qry_payload, indent=2))
    result = requests.post(url, json=qry_payload, headers=headers)
    print(result)
    print(json.dumps(result.json(), indent=2))