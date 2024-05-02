import pytest
import logging


@pytest.fixture
def log():
    logger = logging.getLogger()
    return logger
