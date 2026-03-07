from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class LoginPage():
    txt_username_id = (By.ID,"user-name")
    txt_password_id = (By.ID,"password")
    btn_login_id = (By.ID,"login-button")

    def __init__(self, driver: WebDriver):
        self.driver = driver
    def setusername(self,username):
        uname = self.driver.find_element(*self.txt_username_id)
        uname.clear()
        uname.send_keys(username)
    def setpassword(self,password):
        pwd = self.driver.find_element(*self.txt_password_id)
        pwd.clear()
        pwd.send_keys(password)
    def clicklogin(self):
        self.driver.find_element(*self.btn_login_id).click()
