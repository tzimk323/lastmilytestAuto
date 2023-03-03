from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from features.pageobjects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumpagefactory import PageFactory
import abc
import unittest


class RegisterPage(BasePage):

    #    Locators

    passwordRegister: WebElement
    nameRegister: WebElement
    companyName: WebElement
    usernameRegisterCSS: WebElement
    countryPrefix: WebElement
    closeregister: WebElement
    gotoRegister: WebElement
    phone: WebElement
    mailConfirmation: WebElement
    startDemo: WebElement
    startCompany: WebElement
    loginLink: WebElement


    driver: WebDriver

    locators = {
        'passwordRegister': ('id', "password"),
        'nameRegister': ('id', 'name'),
        'companyName': ('id', 'companyName'),
        'usernameRegisterCSS': ('css', "input[type='email']"),
        'countryPrefix': ('id', 'countryPrefix'),
        'loginLink': ('id', 'loginLink'),
        'closeregister': ('id', "close-register"),
        'gotoRegister': ('id', 'gotoRegister'),
        'phone': ('id', 'telephone-stop-point-form'),
        'mailConfirmation': ('id', "mail-confirmation"),
        'startDemo': ('id', 'startDemo'),
        'startCompany': ('id', 'startCompany')

    }

    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.phone.is_displayed())

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators['phone'])

    def waitMailConfirmationDisplayed(self):
        self.waitElementDisplayed(self.locators['mailConfirmation'])



    def fillRegisterNameField(self, value):
        self.nameRegister.send_keys(value)

    def fillRegisterCompanyNameField(self, value):
        self.companyName.send_keys(value)

    def fillRegisterEmailField(self, value):
        self.usernameRegisterCSS.send_keys(value)

    def fillRegisterPasswordField(self, value):
        self.passwordRegister.send_keys(value)

    def fillRegisterPhoneField(self, value):
        self.phone.send_keys(value)

    def clickRegisterGoButton(self):
        self.gotoRegister.click()

    def clickLoginLink(self):
        self.loginLink.click()
