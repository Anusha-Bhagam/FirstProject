from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginsPage:
    txt_email_name = "Email"
    txt_pwd_name = "Password"
    button_login_xpath = "//*[text()='Log in']"
    link_logout_xpath = "//*[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.NAME, self.txt_email_name).clear()
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.NAME, self.txt_pwd_name).clear()
        self.driver.find_element(By.NAME, self.txt_pwd_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()


    def click_logout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
