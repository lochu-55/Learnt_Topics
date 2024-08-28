from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach",True)
from Elements.WEB_elements import Locators
obj = Locators()

class automate_web:

    def __init__(self,url):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url)

    def close_web(self):
        self.driver.close()

    def enter_username(self,user_input):
        self.driver.find_element(By.ID,obj.USER_NAME).send_keys(user_input)

    def enter_password(self,user_input):
        self.driver.find_element(By.ID,obj.PASS_WORD).send_keys(user_input)

    def click_submit(self):
        self.driver.find_element(By.XPATH,obj.LOG_IN).click()