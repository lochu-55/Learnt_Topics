#from pywinauto.application import Application
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach",True)
options.add_argument("--headless")
import logging


# @pytest.fixture()
# def fix():
#     driver = webdriver.Chrome()
#     yield driver
#     print("after yield")
# class automate_gui:
#     def __init__(self):
#         self.app = Application().start("notepad.exe")
#         self.main_dlg = self.app.UntitledNotepad
#         self.main_dlg.maximize()
#         self.logger = logging.getLogger('my_logger')
#         self.logger.setLevel(logging.DEBUG)
#         self.file_handler = logging.FileHandler(r"C:\Users\vlab\Desktop\Frame_works\Logs\gui_logfile.log",mode="w")
#         self.file_handler.setLevel(logging.DEBUG)
#         self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         self.file_handler.setFormatter(self.formatter)
#         self.logger.addHandler(self.file_handler)

#     def Save_as(self,file_name):
#         self.main_dlg.menu_select("File->SaveAs")
#         save_as_dialog = self.app.SaveAs
#         save_as_dialog.Edit.type_keys(file_name)
#         #save_as_dialog.print_control_identifiers()
#         save_as_dialog.Save.click_input()
#         confirm_save_as = self.app.ConfirmSaveAs
#         if confirm_save_as.is_visible():
#             confirm_save_as.Yes.click_input()

#     def select_menu(self,menu_item):
#         self.main_dlg.menu_select(menu_item)


#     def edit(self,text):
#         self.edit = self.main_dlg.child_window(class_name="Edit")
#         self.edit.set_text(text)

#     def close_gui(self):
#         self.app.kill()

#     def enter_username(self,driver):
#         driver.get("https://practicetestautomation.com/practice-test-login/")




from Web_elements.login_page import Locators
obj = Locators()

class automate_web:

    def __init__(self,url):
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(url)
        self.driver.maximize_window()
        self.logger = logging.getLogger('my_logger')
        self.logger.setLevel(logging.DEBUG)
        self.file_handler = logging.FileHandler("/var/lib/jenkins/workspace/job_sri/Frame_works/Logs/web_logfile.log", mode="w")
        self.file_handler.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

    def close_web(self):
        self.driver.close()

    def enter_username(self,user_input):
        self.driver.find_element(By.ID,obj.USER_NAME).send_keys(user_input)

    def enter_password(self,user_input):
        self.driver.find_element(By.ID,obj.PASS_WORD).send_keys(user_input)

    def click_submit(self):
        self.driver.find_element(By.XPATH,obj.LOG_IN).click()














