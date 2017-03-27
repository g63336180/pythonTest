#!/usr/local/bin/python3

import requests

resp = requests.get("http://www.0478xinxi.com")

print(resp.status_code)
