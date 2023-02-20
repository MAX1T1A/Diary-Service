import os

import requests


SERVER_DOCKER_URL = "http://0.0.0.0/api/v1/"
register_url = "register/"

params = {
  "name": "max1t1a",
  "email": "max1t1a@example.com",
  "password": "stringst",
  "password2": "stringst"
}

response = requests.post(
    os.path.join(SERVER_DOCKER_URL, register_url),
    params=params
)

if __name__ == "__main__":
    print(response.status_code)
