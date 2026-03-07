from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage():
    msg_productpage_xpath = (By.XPATH, "//span[@class='title']")
    btn_menu_xpath= (By.XPATH,"//*[@id='react-burger-menu-btn']")
    lnk_logout_id = (By.ID, "logout_sidebar_link")

    def __init__(self, driver: WebDriver):
        self.driver = driver
    def isProductPageExists(self):
        try:
            return self.driver.find_element(*self.msg_productpage_xpath).is_displayed()
        except:
            return False
    def clickmenu(self):
        self.driver.find_element(*self.btn_menu_xpath).click()
    def clicklogout(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.lnk_logout_id))
        element.click()
