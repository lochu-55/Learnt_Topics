import json
import jsonschema
from core.libs.API import Methods
from core.utils.logs import CustomLogging


class DataTransfer:
    def __init__(self, filename):
        self.data = []  # Create an empty list to store
        self.filename = filename

    def read_data(self):
        with open(self.filename, 'r') as json_file:
            users_data = json.load(json_file)

        for person in users_data['person']:
            if person['id'] is not None:
                person_dict = {
                    'name': person['name'],
                    'email': person['email'],
                    'gender': person['gender'],
                    'status': person['status'],
                    'id': person['id']
                }
            else:
                person_dict = {
                    'name': person['name'],
                    'email': person['email'],
                    'gender': person['gender'],
                    'status': person['status'],
                    'id': None
                }
            self.data.append(person_dict)

    def write_data(self):
        with open(self.filename, 'w') as json_file:
            json.dump({"person": self.data}, json_file, indent=4)


class ApiTests:

    def __init__(self, response):
        self.response = response

    def status_code(self, expected_output):
        if self.response.status_code == expected_output:
            return 0
        else:
            return 1

    def response_time(self, expected_output):
        if self.response.elapsed.total_seconds() < expected_output:
            return 0
        else:
            return 1

    def content_type(self, expected_output):
        if self.response.headers["Content-Type"].startswith(expected_output):
            return 0
        else:
            return 1

    def body_size(self, expected_output):
        if len(self.response.content) < expected_output:
            return 0
        else:
            return 1

    def json_schema_validation(self, expected_schema_file_path):
        try:
            with open(expected_schema_file_path, 'r') as schema_file:
                schema = json.load(schema_file)
            json_response = self.response.json()
            jsonschema.validate(instance=json_response, schema=schema)
            return 0
        except (jsonschema.ValidationError, jsonschema.SchemaError) as e:
            return f"JSON schema validation failed: {e}"
        except ValueError:
            return "Error parsing response JSON"
        except FileNotFoundError:
            return "Schema file data.schema.json not found"

    def status_code_text(self, expected_text: str):
        if self.response.reason == expected_text:
            return 0
        else:
            return 1

    def header_present(self, header_name: str):
        if header_name in self.response.headers:
            return 0
        else:
            return 1

    def header_value(self, header_name: str, expected_value: str):
        if self.response.headers.get(header_name) == expected_value:
            return 0
        else:
            return 1

    def cookie_present(self, cookie_name: str):
        if cookie_name in self.response.cookies:
            return 0
        else:
            return 1

    def cookie_value(self, cookie_name: str, expected_value: str):
        if self.response.cookies.get(cookie_name) == expected_value:
            return 0
        else:
            return 1

    def response_type(self, expected_type: type):
        if isinstance(self.response, expected_type):
            return 0
        else:
            return 1

    def json_fields(self, expected_fields: dict):
        json_response = self.response.json()
        if json_response == expected_fields:
            return 0
        else:
            return 1

    def json_field(self, field: str, expected_value):
        json_response = self.response.json()
        value = json_response.get(field)
        if value == expected_value:
            return 0
        else:
            return 1

    def get_id_from_response(self):
        try:
            json_data = self.response.json()
            return json_data.get('id')
        except ValueError:
            raise AssertionError("Error parsing response JSON")
