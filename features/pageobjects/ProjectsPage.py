from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from features.pageobjects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumpagefactory import PageFactory
import abc
import unittest

from selenium import webdriver


class ProjectsPage(BasePage):
    newProjectButton: WebElement
    projectBox: WebElement
    projectTitle: WebElement
    driver: WebDriver

    locators = {
        'newProjectButton': ('id', "new-project-button"),
        'projectBox': ('id', 'project-box'),
        'projectTitle': ('id', 'project-title')
    }

    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.newProjectButton.is_displayed())

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators.get("projectBox"))

        # self.waitElementDisplayed(self.locators.get('newProjectButton'))

    """Page Actions"""

    def ichooseProjectWithName(self, projectName):
        projectTitles = self.driver.find_elements(self.locators['projectBox'][0],self.locators['projectBox'][1])
        for project in projectTitles:
            if projectName in project.text:
                project.find_element(By.ID,'project-title').click()

    def ichooseProjectWithOrder(self, number):
        projectTitles = self.driver.find_elements(self.locators['projectBox'][0],self.locators['projectBox'][1])
        counter=1
        for project in projectTitles:
            if counter == int(number):
                project.find_element(By.ID,'project-title').click()
            counter=counter+1
