import pytest
from Framework.Utilities.Logging import Logger

@pytest.fixture
def log():
    logger= Logger(r"Logs/API_logs/API.log")
    return logger