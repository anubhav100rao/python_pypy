import requests
from pprint import pprint

URL = "https://httpbin.org/get"


params = {
    "name": "Anubhav",
    "age": 23
}
"""

URL_POST = "https://httpbin.org/post"

payload = {
    "name": "Anubhav",
    "age": 23
}

post_response = requests.post(URL_POST, data=payload)
pprint(post_response.json())
"""

response = requests.get(URL, params=params)

data = response.json()
del data['origin']
pprint(data)