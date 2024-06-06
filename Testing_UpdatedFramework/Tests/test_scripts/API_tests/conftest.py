import pytest
from Core.utils.logging import logger


@pytest.fixture
def log():
    logs = logger(r"Core/utils/Logs/API_logs/API.log")
    return logs
