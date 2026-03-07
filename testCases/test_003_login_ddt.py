import os.path
import time

from pageObjects.LoginPage import LoginPage
from pageObjects.ProductPage import ProductPage
from utilities import ExcelUtils
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_Login_DDT():
    baseurl=ReadConfig.getApplicationURL()
    logger= LogGen.loggen()
    path= os.path.abspath(os.curdir)+"\\testData\\LoginData.xlsx"

    def test_login_ddt(self,setup):
        self.logger.info("*** Starting Test_003_Login_DataDriven ***")
        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.pp=ProductPage(self.driver)
        for r in range(2, self.rows+1):
            self.username=ExcelUtils.readData(self.path,'Sheet1', r, 1)
            self.pwd= ExcelUtils.readData(self.path, 'Sheet1',r,2)
            self.exp= ExcelUtils.readData(self.path, 'Sheet1',r,3)
            self.lp.setusername(self.username)
            self.lp.setpassword(self.pwd)
            self.lp.clicklogin()
            time.sleep(3)
            self.targetpage=self.pp.isProductPageExists()
            if self.exp=='Valid':
                if self.targetpage==True:
                    lst_status.append("Pass")
                    self.pp.clickmenu()
                    self.pp.clicklogout()
                else:
                    lst_status.append("Fail")
            elif self.exp=='Invalid':
                if self.targetpage==True:
                    lst_status.append("Fail")
                    self.pp.clickmenu()
                    self.pp.clicklogout()
                else:
                    lst_status.append("Pass")
            else:
                lst_status.append("Pass")
        self.driver.close()
        if "Fail" not in lst_status:
            self.logger.info("DDT Test Passed")
            assert True
        else:
            self.logger.info("DDT Test Failed")
            assert False
        self.logger.info("******* End of test_003_login_Datadriven **********")


