from utils.myconfigparser import *
from utils.oops_configparser import Configparser

def test_getgmailurl():
    print(getgmailurl())

def test_getoutlookpass():
    config = Configparser()
    print(config.getoutlookpass())