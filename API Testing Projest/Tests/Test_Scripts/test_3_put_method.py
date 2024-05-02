import pytest
from Framework.libraries.Base import Methods
from Framework.Data.dataobjects import Objects
import jsonschema
import json

c = 0


@pytest.fixture
def response():
    global c
    met = Methods()
    old_conf = Objects(r"../../Framework/Data/data.json")
    old_conf.read_data()
    new_conf = Objects(r"../../Framework/Data/new_data.json")
    new_conf.read_data()
    payload = new_conf.data[c]
    value = old_conf.data[c]["id"]
    res = met.put(id=value, data=payload)
    yield res
    c += 1


def test_put_request_status_code(response, log):
    log.info("tested status code")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"


def test_put_request_response_time(response, log):
    log.info("tested response time")
    assert response.elapsed.total_seconds() < 5, "Response time exceeds 1 second"


def test_put_request_content_type(response, log):
    log.info("tested context type")
    assert response.headers["Content-Type"].startswith("application/json"), "Unexpected Content-Type"


def test_put_request_body_size(response, log):
    log.info("tested body size")
    assert len(response.content) < 1024, "Response body size exceeds 1024 bytes"


def test_put_request_json_schema_validation(response, log):
    try:
        with open(r"../../Framework/Data/data.schema.json", 'r') as schema_file:
            schema = json.load(schema_file)

        json_response = response.json()
        jsonschema.validate(instance=json_response, schema=schema)
        log.info("tested json schema")
    except (jsonschema.ValidationError, jsonschema.SchemaError) as e:
        pytest.fail(f"JSON schema validation failed: {e}")
    except ValueError:
        pytest.fail("Error parsing response JSON")
    except FileNotFoundError:
        pytest.fail("Schema file data.schema.json not found")
