<<<<<<< HEAD
import pytest
from Base.Libraries.logging import logger


@pytest.fixture
def log():
    logs = logger(r"Base/utils/Logs/API_logs/API.log")
    return logs
=======
import pytest
from Base.Libraries.logging import logger


@pytest.fixture
def log():
    logs = logger(r"Base/utils/Logs/API_logs/API.log")
    return logs
>>>>>>> 6ddf5bfaa9da0da3c93a81a016f451a9a91e29b9
