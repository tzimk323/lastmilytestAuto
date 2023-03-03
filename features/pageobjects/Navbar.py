from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from features.pageobjects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumpagefactory import PageFactory
import abc
import unittest


class Navbar(BasePage):
    projectsPageButton: WebElement
    driversPageButton: WebElement
    vehiclesPageButton: WebElement
    costumersPageButton: WebElement
    wareHousePageButton: WebElement
    stopsPageButton: WebElement
    partnetsPageButton: WebElement
    sendersPageButton: WebElement
    usersPageButton: WebElement
    officeMemberButton: WebElement
    settingsPageButton: WebElement
    loginButton: WebElement
    accountButton: WebElement
    pagesMenu: WebElement
    pagesName: WebElement
    navbar: WebElement
    companyLogoIcon: WebElement
    companyName: WebElement
    collaboratorsPageButton: WebElement


    collaboratorsPartnerPageButton: WebElement
    driver: WebDriver

    locators = {
        'projectsPageButton': ('id', "projectsPageButton"),
        'driversPageButton': ('id', "drivers-nav-link"),
        'vehiclesPageButton': ('id', "vehicles-nav-link"),
        'costumersPageButton': ('id', "costumersPageButton"),
        'wareHousePageButton': ('id', "warehouse-nav-link"),
        'stopsPageButton': ('id', "stops-nav-link"),
        'partnetsPageButton': ('id', "partners-navbar"),
        'sendersPageButton': ('id', "senders-navbar"),
        'usersPageButton': ('id', "userOptions"),
        'officeMemberButton': ('id', "officeMemberButton"),
        'settingsPageButton': ('id', "settings-button"),
        'loginButton': ('id', "login-nav-link"),
        'collaboratorsPageButton': ('id', "collaborators-navbar"),
        'collaboratorsPartnerPageButton': ('id', "collaborator-partners-page"),



        'accountButton': ('id', "account-drop-down"),
        'pagesMenu': ('id', "pagesMenu"),
        'pagesName': ('id', "pageName"),

        'navbar': ('id', "navbar"),
        'companyLogoIcon': ('id', "companyLogo"),
        'companyName': ('id', "companyNameButton"),

    }

    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.projectsPageButton.is_displayed())

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators.get('projectsPageButton'))

    """Page Actions"""

    def clickProjectButton(self):
        self.projectsPageButton.click()

    def clickPartnersPageButton(self):
        self.partnetsPageButton.click()
    def clickCustomersPageButton(self):
        self.costumersPageButton.click()

    def clickSendersPageButton(self):
        self.sendersPageButton.click()

    def clickSettingsPageButton(self):
        self.settingsPageButton.click()

    def clickCollaboratorsPageButton(self):
        self.collaboratorsPageButton.click()

    def clickCollaboratorsPartnersPageButton(self):
        self.collaboratorsPartnerPageButton.click()
