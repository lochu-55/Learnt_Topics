import pytest
from Base.Libraries.API_Base import Methods
from Tests.API_tests import test_1_post_method as delete


delete.obj.read_data()


@pytest.fixture(params=delete.obj.data)
def response(request):
    met = Methods()
    value = request.param["id"]
    res = met.delete(id=value)
    return res

@pytest.mark.api
def test_delete_request_status_code(response):
    delete.log.logger.info("tested status code")
    assert response.status_code == 204, f"Unexpected status code: {response.status_code}"
