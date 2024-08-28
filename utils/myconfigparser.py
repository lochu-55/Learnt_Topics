import configparser
from pathlib import Path
cfgfile = 'qa.ini'
cfgfiledir = 'config'

config = configparser.ConfigParser()

basedir = Path(__file__).resolve().parent.parent
config_file = basedir.joinpath(cfgfiledir).joinpath(cfgfile)

config.read(config_file)

def getgmailurl():
    return config['gmail']['url']

def getgmailuser():
    return config['gmail']['user']

def getgmailpass():
    return config['gmail']['pass']