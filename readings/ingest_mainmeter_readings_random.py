import requests
import json
from settings.loader import load_env
import os
from datetime import datetime, timedelta, date
import pytz, random

# Same as other sample on main meter, just generates a larger number of random values
def generate_readings():
    reads=[]
    from_date = (datetime.now() + timedelta(days=-20))  #20 days back in time and hourly until yesterday
    from_date = from_date.astimezone(pytz.utc).replace(hour=0, minute=0, second=0)
    to_date = (datetime.today() + timedelta(days=-1))
    to_date = to_date.astimezone(pytz.utc).replace(hour=0, minute=0, second=0)
    while from_date<to_date:
        value = random.uniform(3472.5, 3492.9)   #Random between these numbers
        from_date = from_date + timedelta(hours=1)
        reads.append({
              "timestamp": datetime.utcfromtimestamp(from_date.timestamp()).strftime('%Y-%m-%dT%H:%M:%SZ'),
              "value": "%.2f" % value
            })
    return reads

sample_readings={
    "meters": [
    {
      "id": "121212121212",
      "registers": [
        {
          "id": "active_power",
          "values": generate_readings()
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

if __name__ == '__main__':
    load_env()
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")
    ingest_mainmeter_readings(server_url, token)