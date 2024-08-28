import requests
import json


class Methods:
    def __init__(self, file_path, loggre):

        # Load JSON data from file
        with open(file_path, 'r') as json_file:
            api_config = json.load(json_file)

        # Extract URL and authorization token
        self.url = api_config['scheme'] + api_config['host'] + api_config['path']
        self.authorization = 'Bearer ' + api_config['authorization_token']
        self.logger = loggre

    def get_records(self):
        try:
            r = requests.get(url=self.url, headers={"Authorization": self.authorization})
            r.raise_for_status()  # Raise an error for non-2xx responses
            return r
        except requests.exceptions.RequestException as e:
            return None

    def get_record(self, id):
        try:
            endpoint = f"{self.url}/{id}"
            r = requests.get(url=endpoint, headers={"Authorization": self.authorization})
            r.raise_for_status()
            return r
        except requests.exceptions.RequestException as e:
            return None

    def put(self, id, data):
        try:
            endpoint = f"{self.url}/{id}"
            r = requests.put(url=endpoint, headers={"Authorization": self.authorization}, json=data)
            r.raise_for_status()
            return r
        except requests.exceptions.RequestException as e:
            return None

    def post(self, data):
        try:
            r = requests.post(url=self.url, headers={"Authorization": self.authorization}, json=data)
            r.raise_for_status()
            return r
        except requests.exceptions.RequestException as e:
            return None

    def delete(self, id):
        try:
            endpoint = f"{self.url}/{id}"
            r = requests.delete(url=endpoint, headers={"Authorization": self.authorization})
            r.raise_for_status()
            return r
        except requests.exceptions.RequestException as e:
            return None
