from datetime import time
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from features.pageobjects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumpagefactory import PageFactory
import abc
import unittest


class ProjectDaysPage(BasePage):
    newProjectDayButton: WebElement
    projectDaysContainer: WebElement
    projectProblemChart: WebElement
    newProjectDayModal: WebElement

    newDayTitleField: WebElement
    newDayModalGoButton: WebElement

    locators = {
        'newProjectDayButton': ('id', "new-project-day-button"),
        'projectDaysContainer': ('id', 'project-days-grid-container'),
        'newProjectDayModal': ('id', 'create-project-first-step-modal'),
        'newDayTitleField': ('id', 'project-title'),
        'newDayModalGoButton': ('id', 'project-goButton'),


    }

    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.projectDaysContainer.is_displayed()

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators['projectDaysContainer'])
        self.waitPageToLoad() # time.sleep(3)

    def waitNewDayModalVisible(self):
        self.waitElementDisplayed(self.locators['newProjectDayModal'])
        self.waitPageToLoad() # time.sleep(3)

    def waitNewDayModalNotVisible(self):
        self.waitElementNotDisplayed(self.locators['newProjectDayModal'])
        self.waitPageToLoad() # time.sleep(3)


    def ichooseProjectDayWithTitle(self, daysTitle):
        # daysTitle="gfjnr"
        time.sleep(1)
        projectDay = self.projectDaysContainer.find_element(By.CSS_SELECTOR, f"div[title='{daysTitle}']")
        projectDay.click()

        return self

    def clickNewProjectDayButton(self):
        self.newProjectDayButton.click()

    def setNewDayTile(self,name):
        self.setTextField(self.newDayTitleField,name)

    def clickNewDayModalGoBUtton(self):
        self.newDayModalGoButton.click()


    def getTitlesAndCellDetailsWithTitle(self, daysTitle):
        # daysTitle="gfjnr"

        array = []
        projectDay = self.projectDaysContainer.find_element(By.CSS_SELECTOR, f"div[title='{daysTitle}']")
        elements = projectDay.find_elements(By.XPATH, "../../../div")

        # skip first and last
        for cell in elements[1:-1]:
            array.append(cell.text.replace("\n", " "))
        return array
