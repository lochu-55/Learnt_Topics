import pytest
from Base.GUIWEB import automate_web
from time import sleep
global web_obj


@pytest.fixture(scope='module')
def web():
    web_obj = automate_web("https://practicetestautomation.com/practice-test-login/")
    web_obj.logger.info("opening website")
    yield web_obj

@pytest.mark.selenium
def test_login(web):
    web.logger.info("entering username")
    web.enter_username("student")
    web.logger.info("entering password")
    web.enter_password("Password123")
    web.click_submit()

@pytest.mark.selenium
def test_close(web):
    web.logger.info("closing website")
    web.close_web()