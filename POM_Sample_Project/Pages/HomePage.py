from selenium.webdriver.common.by import By
from Locators.locators import Locate
from Pages.LoginPage import LoginPage
class HomePage:

    def __init__(self,driver):
        self.driver = driver
        self.login = LoginPage(driver)
        self.welcome_link = Locate.welcome_link
        self.logout_linkText = Locate.logout_linkText

    def click_welcome(self):
        self.driver.find_element(By.XPATH,self.welcome_link).click()
        self.login.logger.info("clicking the welcome link")

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_linkText).click()
        self.login.logger.info("clicking logout")

