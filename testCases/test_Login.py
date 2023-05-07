from pageObjects.LoginPage import LoginsPage
from Utlities.readProperties import ReadConfig
from Utlities.CustomLogger import LogGen
import pytest


class TestLogin:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.logged()

    @pytest.mark.sanity
    def test_home_page(self, setup):
        self.logger.info("*********TEST1***************")
        self.logger.info("********HOME PAGE TEST*******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == 'Your store. Login':

            assert True
            self.driver.close()
            self.logger.info("********HOME PAGE TEST PASSED*******************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "homepage.png")
            self.driver.close()
            self.logger.info("********HOME PAGE TEST FAILED*******************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********LOGIN PAGE TEST *******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginsPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title

        if act_title == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
            self.logger.info("********LOGIN PAGE TEST PASSED*******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("********LOGIN PAGE TEST FAILED*******************")
            assert False
