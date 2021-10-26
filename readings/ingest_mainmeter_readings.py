import requests
import json
from settings.loader import load_env
import os
sample_readings={
    "meters": [
    {
      "id": "12121212121212",
      "registers": [
        {
          "id": "active_power",
          "values": [
            {
              "timestamp": "2020-05-17T21:25:00Z",
              "value": "3492.0"
            }
          ]
        }
      ]
    }
    ]
},


# Format used in Sthlmflex for main smart meter readings.
# Readings are attached to the one single asset behind the meter on the server side.
def ingest_mainmeter_readings(server_url, token, readings=sample_readings):
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/assetdata/ingest_readings_sthlmflex/'
    payload=readings

    print(json.dumps(payload, indent=2))
    result = requests.post(url, json=payload, headers=headers)
    print(result)
    print(json.dumps(result.json(), indent=2))