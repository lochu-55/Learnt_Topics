from selenium.webdriver.common.by import By
from Locators.locators import Locate
import logging
import os
class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_txtbox = Locate.username_txtbox
        self.password_txtbox = Locate.password_txtbox
        self.LoginBtn = Locate.LoginBtn

        self.logger = logging.getLogger(__name__)
        self.fh = logging.FileHandler(filename="C:/Users/vlab/PycharmProjects/POM_Sample_Project/Logs/webapp.log", mode='w')
        self.frmt = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s")
        self.fh.setFormatter(self.frmt)
        self.logger.addHandler(self.fh)
        self.logger.setLevel(logging.DEBUG)

    def enter_username(self,username):
        self.driver.find_element(By.NAME,self.username_txtbox).clear()
        self.logger.info("clear the username text box")
        self.driver.find_element(By.NAME, self.username_txtbox).send_keys(username)
        self.logger.info("entering the username")

    def enter_password(self,password):
        self.driver.find_element(By.NAME, self.password_txtbox).clear()
        self.logger.info("clear the password text box")
        self.driver.find_element(By.NAME, self.password_txtbox).send_keys(password)
        self.logger.info("entering the password")

    def click_login(self):
        self.driver.find_element(By.XPATH,self.LoginBtn).click()
        self.logger.info("clicking the login button")
