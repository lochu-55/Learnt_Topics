import pytest
import pytest_html
from pywinauto.application import Application
from selenium import webdriver
import logging
import os


class Logging:

    def __init__(self, filename):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.filename = filename
        raw_str = r"C:\Users\vlab\PycharmProjects\GFWBV_02\Utils"
        self.file_handler = logging.FileHandler(f"{raw_str}\\Logs\\{self.filename}_logs")
        self.file_handler.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

    def log_msg(self, msg):
        self.logger.info(msg)

class WinGuiAuto(Logging):

    def __init__(self, filename):
        super().__init__(filename)
        self.path = "notepad.exe"
        self.app = Application(backend='uia').start(self.path)

    def close_gui(self):
        self.app.kill()


class WebGuiAuto(Logging):
    def __init__(self, filename, url):
        super().__init__(filename)
        self.driver = webdriver.Chrome()
        self.url = url

    def chrome(self):
        self.driver.get(self.url)

    def firefox(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

    def edge(self):
        self.driver = webdriver.Edge()
        self.driver.get(self.url)

    def close_web(self):
        self.driver.close()
