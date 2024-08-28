<<<<<<< HEAD
from selenium.webdriver.common.by import By
class Locators:
    URL = "https://practicetestautomation.com/practice-test-login/"
    USER_NAME = (By.ID,"username")
    PASS_WORD = (By.ID,"password")
    LOG_IN = (By.XPATH,"//button[@id='submit']")
    PATH = r"C:\Users\vlab\Desktop\final_Framework\final_Framework\Base\utils\Screenshots\WEB_SS"
    LOG_PATH1=r"C:\Users\vlab\Desktop\final_Framework\final_Framework\Base\utils\Logs\WEB_logs\web.log"


class inputs:
    user = "student"
=======
from selenium.webdriver.common.by import By
class Locators:
    URL = "https://practicetestautomation.com/practice-test-login/"
    USER_NAME = (By.ID,"username")
    PASS_WORD = (By.ID,"password")
    LOG_IN = (By.XPATH,"//button[@id='submit']")
    PATH = r"Base\utils\Screenshots\WEB_SS"
    LOG_PATH1=r"Base\utils\Logs\WEB_logs\web.log"


class inputs:
    user = "student"
>>>>>>> 6ddf5bfaa9da0da3c93a81a016f451a9a91e29b9
    pswd = "Paword123"