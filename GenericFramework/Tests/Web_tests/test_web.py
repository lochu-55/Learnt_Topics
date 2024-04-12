import pytest
from Framework.Web import Login

@pytest.fixture(scope='module')
def L():
    obj = Login(__name__)
    obj.chrome()
    yield obj

@pytest.mark.selenium
def test_login(L):
    L.log_msg("entering username")
    L.enter_username("standard_user")
    L.log_msg("entering password")
    L.enter_password("secret_sauce")
    L.click_submit()


@pytest.mark.selenium
def test_close(L):
    L.log_msg("closing website")
    L.close_web()
