from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from features.pageobjects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
from seleniumpagefactory import PageFactory
import abc
import unittest


class LoginPage(BasePage):

    #    Locators
    user_name: WebElement
    password: WebElement
    login_btn: WebElement
    registerButton: WebElement
    driver: WebDriver

    locators = {
        'user_name': ('id', "username"),
        'password': ('id', 'password'),
        'login_btn': ('id', 'gobutton'),
        'registerButton': ('id', 'registerButton')
    }

    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.emailLocatorID.is_displayed())

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators['login_btn'])
        sleep(2)

    def clickf(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def waitElementDisplayed(self, by_locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator))

    """Page Actions"""

    def open(self, url):
        self.driver.get(url)

    def clickLoginButton(self):
        self.driver.user_name.click()

    def fillLoginUserNameWith(self, text):
        self.user_name.send_keys(text)

    def fillPassWordWith(self, text):
        self.password.send_keys(text)
        # self.user_name.send_keys(text)

    def clickLoginButton(self):
        self.login_btn.click()


    def clickLoginPageRegisterButton(self):
        self.registerButton.click()



    # def setName(self, name):
    #     self.type("name_XPATH", name)
    #
    # def setPhoneNumber(self, phoneNum):
    #     self.type("phone_XPATH", phoneNum)
    #
    # def setEmail(self, email):
    #     self.type("email_XPATH", email)
    #
    # def setCountry(self, country):
    #     self.select("country_XPATH", country)
    #
    # def setCity(self, city):
    #     self.type("city_XPATH", city)
    #
    # def setUsername(self, username):
    #     self.type("username_XPATH", username)
    #
    # def setPassword(self, password):
    #     self.type("password_XPATH", password)
    #
    # def submitForm(self):
    #     self.click("submit_XPATH")
