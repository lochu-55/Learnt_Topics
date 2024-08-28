import pytest
from Framework.libraries.Base import Methods
from Framework.Data.dataobjects import Objects

obj = Objects(r"../../Framework/Data/data.json")
obj.read_data()


@pytest.fixture(params=obj.data)
def response(request):
    met = Methods()
    value = request.param["id"]
    res = met.delete(id=value)
    return res


def test_delete_request_status_code(response, log):
    log.info("tested status code")
    assert response.status_code == 204, f"Unexpected status code: {response.status_code}"
