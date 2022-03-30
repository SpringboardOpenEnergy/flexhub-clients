import json

import requests

sample_readings=[{"val": 44, "time": "2021-02-01T21:00:00Z"},
{"val": 45, "time": "2021-02-22:00:00Z"},
{"val": 44, "time": "2021-02-23:00:00Z"}
             ]

# Use this API for registering meter readings directly on assets
# In particular if there are multiple assets behind the meter, this is the API that should be used
def ingest_assetlevel_readings(server_url, token, asset_id, readings=sample_readings):
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/assetdata/ingest_readings_utcformat/'
    payload={
        'asset_id':asset_id,
        'first':readings[0]['time'],
        'last': readings[len(readings)-1]['time'],
        'readings':readings
    }

    print(json.dumps(payload, indent=2))
    result = requests.post(url, json=payload, headers=headers)
    print(result)
    print(json.dumps(result.json(), indent=2))