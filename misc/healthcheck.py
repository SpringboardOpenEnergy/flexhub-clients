import json
import os

import requests

from settings.loader import load_env


def exec_healthcheck(server_url):
    url= server_url + '/api/healthcheck/'
    result = requests.get(url)
    print(result)
    print(json.dumps(result.json(), indent=2))
    if len(result.json())==0:
        return None
    return result.json()  # For simplicity in sample, select first company - most common case is only 1

if __name__ == '__main__':
    load_env()
    server_url = os.environ.get("server_url")
    exec_healthcheck (server_url)