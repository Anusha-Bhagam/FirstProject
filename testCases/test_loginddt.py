import time

from pageObjects.LoginPage import LoginsPage
from Utlities.readProperties import ReadConfig
from Utlities.CustomLogger import LogGen
from Utlities import ExcelUtils
import pytest


class TestLoginddt:
    baseURL = ReadConfig.get_application_url()
    path = ".//TestData/Book1.xlsx"
    logger = LogGen.logged()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginsPage(self.driver)
        lst_status = []
        self.rows = ExcelUtils.get_row_count(self.path, 'Sheet1')

        for r in range(2,self.rows+1):
            self.uname = ExcelUtils.read_data(self.path,'Sheet1',r,1)
            self.passwrd = ExcelUtils.read_data(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.read_data(self.path, 'Sheet1', r, 3)


            self.lp.set_username(self.uname)
            self.lp.set_password(self.passwrd)
            self.lp.click_login()
            time.sleep(5)
            self.act_title = self.driver.title
            self.exp_title = "Dashboard / nopCommerce administration"

            if self.act_title == self.exp_title:
               if self.exp == 'pass':
                   self.lp.click_logout()
                   lst_status.append('pass')
               elif self.exp == 'fail':
                   self.lp.click_logout()
                   lst_status.append('fail')
            elif self.act_title != self.exp_title:
                if self.exp == 'pass':
                    lst_status.append('fail')
                elif self.exp == 'fail':
                    lst_status.append('pass')

        if "fail" not in lst_status:
                self.driver.close()
                assert True
        else:
                self.driver.close()
                assert False








