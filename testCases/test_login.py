import os.path
from pageObjects.LoginPage import LoginPage
from pageObjects.ProductPage import ProductPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Login:
    logger=LogGen.loggen()
    baseURL= ReadConfig.getApplicationURL()
    username= ReadConfig.getUsername()
    password= ReadConfig.getPassword()

    def test_account_reg(self,setup):
        self.logger.info("*** Test_001_Login Started ***")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching URL")
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.pp=ProductPage(self.driver)
        self.logger.info("Logging in with valid credentials")
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("Logging In")
        self.targetpage=self.pp.isProductPageExists()
        if self.targetpage == True:
            self.logger.info("Login Successfull")
            assert True
            self.driver.close()
        else:
            self.logger.error("Login Failed")
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_productpage.png")
            self.driver.close()
            assert False
        self.logger.info("*** Test_001_Login Finished ***")