import HtmlTestRunner


from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from time import sleep
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        cls.login = LoginPage(cls.driver)
        cls.home = HomePage(cls.driver)
        cls.login.logger.info("initiating setup class...")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.login.logger.info("maximizing the window...")



    def test_login_valid(self):


        self.login.enter_username("Admin")

        self.login.enter_password("admin123")
        self.login.click_login()


        self.home.click_welcome()
        self.home.click_logout()

        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test is completed")
        cls.login.logger.info("tearing down the class...")



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))