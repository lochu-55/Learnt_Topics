import pytest
from BaseClass.Framework.Web import automate_web
from time import sleep
global web_obj
import logging

@pytest.fixture(scope='module')
def web():
    web_obj = automate_web("https://practicetestautomation.com/practice-test-login/")
    logging.info("opening website")
    yield web_obj

@pytest.mark.selenium
def test_login(web):
    logging.info("entering username")
    web.enter_username("student")
    logging.info("entering password")
    web.enter_password("Password123")
    web.click_submit()
    sleep(2)

@pytest.mark.selenium
def test_close(web):
    logging.info("closing website")
    web.close_web()