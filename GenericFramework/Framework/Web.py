from Locators.Web_locators import Login_Page as L
from Framework.Base import WebGuiAuto
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Login(WebGuiAuto):
    
    def __init__(self, filename, url=L.URL):
        super().__init__(filename, url)

    def enter_username(self, user_input):
        try:
            self.driver.find_element(By.ID, L.USER_NAME).send_keys(user_input)
        except NoSuchElementException as e:
            print("Element not found", e)

    def enter_password(self, user_input):
        try:
            self.driver.find_element(By.ID, L.PASS_WORD).send_keys(user_input)
        except NoSuchElementException as e:
            print("Element not found", e)

    def click_submit(self):
        try:
            self.driver.find_element(By.XPATH, L.LOG_IN).click()
        except NoSuchElementException as e:
            print("Element not found", e)
            