import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import abc

from seleniumpagefactory import PageFactory

from Utilities import configReader
import logging
from Utilities.LogUtil import Logger
import unittest
from unittest import TestCase

log = Logger(__name__, logging.INFO)

defaultTimeout = configReader.readConfig('automationParams', 'timeout')


class BasePage(abc.ABC, unittest.TestCase, PageFactory, ActionChains):

    def __init__(self, driver):
        self.driver: WebDriver = driver

    @abc.abstractmethod
    def waitPageVisible(self):
        pass

    @abc.abstractmethod
    def isPageDisplayed(self):
        pass

    # def getElement(self, locator):
    #    return self.driver.find_element(By.XPATH, '//button[text()="Some text"]')

    def clickf(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def isElementPresent(self, locator):
        return len(self.driver.find_elements(locator)) > 0

    def waitElementNotDisplayed(self, locator, timeOut=defaultTimeout):
        locator = (locator[0].replace("_", " "), locator[1])
        WebDriverWait(self.driver, timeOut).until_not(EC.visibility_of_element_located(locator),
                                                           "Wait timeout visible , Element should not be displayed")

    def waitElementDisplayed(self, locator, timeOut=defaultTimeout):
        locator = (locator[0].replace("_", " "), locator[1])
        WebDriverWait(self.driver, timeOut).until(EC.presence_of_element_located(locator),
                                                  "Wait timeout presence, Element not found")
        WebDriverWait(self.driver, timeOut).until(EC.visibility_of_element_located(locator),
                                                  "Wait timeout visible , Element not displayed")

    # Notworking
    def waitEitherElementDisplayed(self, locator1,locator2, timeOut=defaultTimeout):
        locator1 = (locator1[0].replace("_", " "), locator1[1])
        locator2 = (locator2[0].replace("_", " "), locator2[1])
        try:
            WebDriverWait(self.driver, timeOut).until(EC.presence_of_element_located(locator1),
                                                      "Wait timeout presence, Element not found")
            WebDriverWait(self.driver, timeOut).until(EC.visibility_of_element_located(locator1),
                                                  "Wait timeout visible , Element not displayed")
        except:
            WebDriverWait(self.driver, timeOut).until(EC.presence_of_element_located(locator2),
                                                      "Wait timeout presence, Element not found")
            WebDriverWait(self.driver, timeOut).until(EC.visibility_of_element_located(locator2),
                                                      "Wait timeout visible , Element not displayed")
    # Not Working
    def waitElementStateChange(self, locator, attribute, text, timeOut=defaultTimeout):
        WebDriverWait(self.driver, timeOut).until(EC.text_to_be_present_in_element_attribute(locator, attribute, text),
                                                  "Wait timeout presence,Attribute didnt change as expected ")

    # Not working yet
    def waitWebElementDisplayed(self, locator, timeOut=defaultTimeout):
        WebDriverWait(self.driver, timeOut).until(self.webElement_displayed(locator))

    def waitPageToLoad(self, timeOut=defaultTimeout):
        WebDriverWait(self.driver, timeOut).until(self.page_has_loaded)
        WebDriverWait(self.driver, timeOut).until(self.javascript_loaded)

    def page_has_loaded(self, lap, **kwargs):
        page_state = self.driver.execute_script("return document.readyState")
        return page_state == 'complete'

    def webElement_displayed(self, lap, locator: WebElement, **kwargs):
        return locator.is_displayed() == True

    def javascript_loaded(self, lap, **kwargs):
        page_state = self.driver.page_source
        time.sleep(0.2)
        return self.driver.page_source == page_state

    def setTextField(self, locator: WebElement, text):
        locator.send_keys(Keys.CONTROL + "A")
        locator.send_keys(Keys.DELETE)
        locator.send_keys(text)

    def setRadioValue(self, locator: WebElement, choice):
        if not locator.is_selected():
            if bool(choice):
                locator.find_element(By.XPATH, "following-sibling::span").click()

    def chooseDropDown(self, locator: WebElement, select):
        locator.click()
        time.sleep(1)
        options_text = {}
        options = locator.find_element(By.CSS_SELECTOR, "ng-dropdown-panel[role='listbox']").find_elements(
            By.CSS_SELECTOR, "div[role='option']")
        for option in options:
            options_text[option.text] = option
        if select in options_text:
            options_text[select].click()
        else:
            raise Exception("Drop down choice does not exist, available choices are :".join(list(options_text.keys())))

    def chooseDropDownTab(self, locator: WebElement, select):
        locator.send_keys(Keys.CONTROL + "A")
        locator.send_keys(Keys.DELETE)
        locator.send_keys(select)
        self.waitPageToLoad()
        time.sleep(2)
        locator.send_keys(Keys.TAB)


    def chooseDropDownType(self, locator: WebElement, select):
        locator.click()
        locator.send_keys(Keys.CONTROL + "A")
        locator.send_keys(Keys.DELETE)
        locator.send_keys(select)
        self.waitPageToLoad()
        time.sleep(2)

        options_text = {}
        options = locator.find_element(By.XPATH, "..").find_element(By.CSS_SELECTOR,
                                                                    "ng-dropdown-panel[role='listbox']").find_elements(
            By.CSS_SELECTOR, "div[role='option']")
        selected = False
        for option in options:
            # options_text[option.text] = option
            if select in option.text:
                option.click()
                selected = True
                break
        if selected == False:
            raise Exception("Drop down choice does not exist, available choices are :".join(list(options_text.keys())))

    def chooseDropDownText(self, locator: WebElement, text):
        locator.click()
        field = locator.find_element(By.CSS_SELECTOR, "input[type='text']")
        field.send_keys(text)
        field.send_keys(Keys.ENTER)

    def setToogleValue(self, locator: WebElement, state):
        state = bool(state)
        if locator.is_selected() != state:
            locator.find_element(By.XPATH, "following-sibling::span").click()

    def setSliderValue(self, locator: WebElement, value, step):
        slider = locator.find_element(By.CSS_SELECTOR, "div[role='slider']")
        slider.click()
        currentValue = int(float(slider.get_attribute("aria-valuenow")))
        difference = currentValue - int(value)
        timesToclick = int(abs(difference / step))
        key = 0
        if difference > 0:
            key = Keys.ARROW_LEFT
        elif difference < 0:
            key = Keys.ARROW_RIGHT
        if key is not 0:
            for click in range(0, timesToclick):
                slider.send_keys(key)
