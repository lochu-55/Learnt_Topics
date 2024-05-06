import pytest
from Framework.Libraries.Web import automate_web
from time import sleep
global web_obj
from Framework.Elements.WEB_elements import inputs,Locators
from Framework.Utilities.Logging import Logger


ip = inputs()
log = Logger(Locators.LOG_PATH1)


@pytest.fixture(scope='module')
def web_obj():
    web_obj = automate_web()
    yield web_obj


@pytest.mark.selenium
def test_login(web_obj):
    log.logger.info("entering username")
    web_obj.enter_username(ip.user)
    log.logger.info("entering password")
    web_obj.enter_password(ip.pswd)


@pytest.mark.selenium
def test_click(web_obj):
    web_obj.click_submit()
    sleep(2)


@pytest.mark.selenium
def test_close(web_obj):
    log.logger.info("closing website")
    web_obj.close_web()
