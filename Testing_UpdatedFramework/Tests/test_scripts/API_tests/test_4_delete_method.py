import pytest
from Testing_Framework.API_Base import Methods
from Tests.test_inputs.API_Data.dataobjects import Objects


obj = Objects(r"Core/Elements/API_Data/data.json")
obj.read_data()


@pytest.fixture(params=obj.data)
def response(request):
    met = Methods()
    value = request.param["id"]
    res = met.delete(id=value)
    return res


@pytest.mark.api
def test_delete_request_status_code(response, log):
    log.logger.info("tested status code")
    assert response.status_code == 204, f"Unexpected status code: {response.status_code}"