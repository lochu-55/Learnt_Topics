import pytest
import os


QA_config = 'qa.prop'
prod_config = 'prod.prop'

def pytest_addoption(parser):
    parser.addoption("--cmdopt",default="QA")

@pytest.fixture()
def CmdOpt(pytestconfig):
    print("\n in c,dopt fixture function..")
    opt = pytestconfig.getoption("cmdopt")

    if opt == 'prod':
        f = open(prod_config, 'r')
    else:
        f = open(QA_config, 'r')

    yield f