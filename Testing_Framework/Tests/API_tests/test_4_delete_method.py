<<<<<<< HEAD
import pytest
from Base.Libraries.API_Base import Methods
from Base.Elements.Data.dataobjects import Objects


obj = Objects(r"Base/Elements/Data/data.json")
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
=======
import pytest
from Base.Libraries.API_Base import Methods
from Base.Elements.Data.dataobjects import Objects


obj = Objects(r"Base/Elements/Data/data.json")
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
>>>>>>> 6ddf5bfaa9da0da3c93a81a016f451a9a91e29b9
    assert response.status_code == 204, f"Unexpected status code: {response.status_code}"