import configparser
from pathlib import Path

class Configparser:
    cfgfile = 'qa.ini'
    cfgfiledir = 'config'

    config = configparser.ConfigParser()

    def __init__(self):
        self.basedir = Path(__file__).resolve().parent.parent
        self.config_file = self.basedir.joinpath(self.cfgfiledir).joinpath(self.cfgfile)
        self.config.read(self.config_file)

    def getgmailurl(self):
        return self.config['gmail']['url']

    def getgmailuser(self):
        return self.config['gmail']['user']

    def getoutlookpass(self):
        return self.config['outlook']['pass']

    def getgmailpass(self):
        return self.config['gmail']['pass']