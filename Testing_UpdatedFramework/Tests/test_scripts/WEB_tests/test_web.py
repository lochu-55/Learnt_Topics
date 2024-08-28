from Core.Libraries.b import pytest
from Testing_Framework.Web import automate_web
from time import sleep
global web_obj
from Tests.test_inputs.WEB_elements import inputs,Locators
from Core.utils.logging import logger

ip = inputs()
log = logger(Locators.LOG_PATH1)
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