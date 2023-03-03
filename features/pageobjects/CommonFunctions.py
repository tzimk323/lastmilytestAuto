import json
from datetime import datetime

import cdp.tracing
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
import string
import random
class CommonFunctions(BasePage):
    driver: WebDriver

    locators = {
        'shipmentsChart': ('id', "shipments-chart"),
    }

    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        pass

    def waitPageVisible(self):
        pass

    def saveDataToDatafile(self,data):
        dataToWrite=json.dumps(data)
        with open(r"dataFiles\ " + 'randomData.txt', "a") as outfile:
            outfile.write(data)
        pass

    def startTracing(self, tab):
        cat = tab.call_method('Tracing.getCategories')
        categories = '-*,blink.console,blink.user_timing,devtools.timeline,disabled-by-default-devtools.screenshot,disabled-by-default-devtools.timeline,disabled-by-default-devtools.timeline.invalidationTracking,disabled-by-default-devtools.timeline.frame,disabled-by-default-devtools.timeline.stack,disabled-by-default-v8.cpu_profiler,disabled-by-default-v8.cpu_profiler.hires,latencyInfo,loading,disabled-by-default-lighthouse,v8.execute,v8'
        tab.call_method('Network.enable')
        tab.call_method('Page.enable')
        tab.call_method('Tracing.start', bufferUsageReportingInterval=500, transferMode="ReportEvents",
                        categories=categories)

    def emaluteCPUthrottleRate(self, tab, rate):
        cat = tab.call_method('Emulation.setCPUThrottlingRate', rate=int(rate))

    def get_random_string(self,length):
        # With combination of lower and upper case
        return ''.join(random.choice(string.ascii_letters) for i in range(length))
        # print random string

    def get_random_number(self, length):
        # With combination of lower and upper case
        return random.randint(1000000000, 9999999999)
        # print random string
    def refreshPage(self):
        self.driver.refresh()