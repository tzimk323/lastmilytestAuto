import json
import time
import timeit
from datetime import datetime
from time import sleep

import cdp.tracing
import pychrome
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

from trio_cdp import open_cdp, page, dom
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from cdp import *
from features.pageobjects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumpagefactory import PageFactory
import abc
import unittest

arrayLog=[]
class ProjectViewPage(BasePage):
    generalSearch: WebElement
    map: WebElement
    optimizeButton: WebElement
    driver: WebDriver
    selectPointsButton: WebElement
    selectDrawPoints: WebElement
    rightClickList: WebElement
    selectStopPointsCounter: WebElement
    middleBarSelection: WebElement
    papakiSymbol: WebElement
    loadingBar: WebElement
    backButton: WebElement
    driversName: WebElement
    vehicleHoverBox: WebElement
    markerHoverBox: WebElement
    createNewStopButton: WebElement
    locators = {
        'generalSearch': ('id', "general-search"),
        'map': ('id', 'map'),
        'optimizeButton': ('id', 'optimize-button'),
        'selectPointsButton': ('id', 'select'),
        'selectDrawPoints': ('id', 'draw-select'),
        'rightClickList': ('xpath',".//div[@class='H_context_menu H_el']"),
        'selectStopPointsCounter': ('id', 'selected-stop-points-count'),
        'middleBarSelection': ('xpath', ".//div[@class='middle-section white-bar-sections']"),
        'loadingBar': ('class_name', 'loading-progress'),
        'backButton': ('id', 'back-button'),
        'papakiSymbol': ('xpath', ".//div[@class='at-divider']"),
        'driversName': ('id', "driver-name-and-last-seen"),
        'vehicleHoverBox': ('id', "vehicle-hover-box"),
        'markerHoverBox': ('id', "marker-hover-box"),
        'createNewStopButton': ('id', "create-new-stop")
    }

    # 'middleBarSelection': ('xpath', ".//div[@class='middle-section white-bar-sections']"),
    # 'loadingBar': ('xpath', ".//div[@class='loading-progress']")
    # 'middleBarSelection': ('class_name', 'middle-section white-bar-sections'),
    # 'loadingBar': ('class_name', 'loading-progress')

    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.optimizeButton.is_displayed())

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators["loadingBar"])
        self.waitElementNotDisplayed(self.locators["loadingBar"])

    def clickOnMapWithOffset(self, x, y):
        actions = ActionChains(self.driver)
        ActionChains(self.driver).move_to_element_with_offset(self.map,x,y).perform()
        ActionChains(self.driver).click().perform()

    def clickCreateNewStopButton(self):
        self.createNewStopButton.click()


    def hoverOnMapWithOffset(self, x, y):
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(self.map,x,y).perform()

    def clickMiddleBarSection(self):
        self.middleBarSelection.click()

    def clickAtPapakiSymbol(self):
        self.papakiSymbol.click()

    def waitRequestBarAppear(self):
        self.waitElementDisplayed(self.locators["loadingBar"])

    def waitRequestBarNotAppear(self):
        self.waitElementNotDisplayed(self.locators['loadingBar'])


    def iClickTheBackButton(self):
        self.backButton.click()

    def rightclickOnMapWithOffset(self, x, y):
        ActionChains(self.driver).move_to_element_with_offset(self.map,x,y).perform()
        ActionChains(self.driver).context_click().perform()
        self.waitElementDisplayed(self.locators['rightClickList'])

    def isVehicleHoverBoxVisible(self):
       return self.vehicleHoverBox.is_displayed()

    def getVehicleHoverBoxTitle(self):
        return self.driversName.text.split("\n")[0]

    def getVehicleHoverBoxLastSeenText(self):
        return self.driversName.text.split("\n")[1]

    def isStopPointHoverBoxVisible(self):
        return self.markerHoverBox.is_displayed()

    def getStopPointHoverBoxTitle(self):
        return self.markerHoverBox.text.split("\n")[0]

    def rightclickOnSpWithOffsetAndKeepTime(self, x, y):
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(self.map,x,y).perform()
        start = timeit.timeit()
        actions.context_click().perform()

        self.waitElementDisplayed(self.locators['rightClickList'])
        end=timeit.timeit()
        time=end-start
        print("The time it took was: "+str(time))
        return time

    def chooseDisableStopPoint(self,choice):
        elements=self.rightClickList.find_elements(By.XPATH,"div")
        for choices in elements:
            if choices.text.lower() == choice.lower():
                ActionChains(self.driver).move_to_element(choices).perform()
                ActionChains(self.driver).click().perform()
                choices.click()



    def changePriorityOfStopPoint(self):
        elements = self.rightClickList.find_elements(By.XPATH,"div")
        for choices in elements:
            if choices.text.lower() == 'high priority'.lower():
                attribute = choices.get_attribute("class")
                if 'clickable' in attribute:
                    ActionChains(self.driver).move_to_element(choices).perform()
                    choices.click()
                    break
            if choices.text.lower() == 'normal priority'.lower():
                attribute = choices.get_attribute("class")
                if 'clickable' in attribute:
                    ActionChains(self.driver).move_to_element(choices).perform()
                    choices.click()
                    break
        self.waitPageToLoad() # time.sleep(2)

    def changeStateOfStopPoint(self):
        elements = self.rightClickList.find_elements(By.XPATH,"div")
        for choices in elements:
            if choices.text.lower() == 'enable'.lower():
                attribute=choices.get_attribute("class")
                if 'clickable' in attribute:
                    ActionChains(self.driver).move_to_element(choices).perform()
                    choices.click()
                    break;
            if choices.text.lower() == 'disable'.lower():
                attribute=choices.get_attribute("class")
                if 'clickable' in attribute:
                    ActionChains(self.driver).move_to_element(choices).perform()
                    choices.click()
                    break;
        self.waitPageToLoad() # time.sleep(2)


    def clickOnMapWithOffsetAndZoomAtScaleAndTimes(self, x, y,times,scale):
        actions = ActionChains(self.driver)

        actions.click_and_hold()
        actions.perform()
        actions.move_by_offset(x, y)
        actions.perform()
        actions.release(self.map)
        actions.perform()
        for i in range(0, int(times)):
            for i in range(0, int(scale)):
                self.driver.find_element(By.ID,'map').click()
                self.driver.find_element(By.ID,'map').click()
                sleep(0.3)
            for i in range(0, int(scale)):
                actions = ActionChains(self.driver)
                actions.context_click(self.map).perform()
                actions.perform()
                sleep(0.3)

    def tracing_complete(trace_data):
        with open("network_trace.json", "w") as f:
            f.write(trace_data)
        print("Tracing complete. Data saved to file.")

    def output_on_end(self, **kwargs):
        # print(kwargs)

        arrayLog.append(kwargs)
        json_object = json.dumps(kwargs)
        logFileName = datetime.now().strftime('Tracing_%H_%M_%d_%m_%Y.json')
        return arrayLog
        # with open(r"Logs\ " + logFileName, "w") as outfile:
        #     outfile.write(json_object)
        # outfile.close()

    def output_on_start(self):
        print("STAAAAAAART")

    def clickDrawPointsButton(self):
        self.selectDrawPoints.click()

    def clickSelectPointsButtonToShowOptions(self):

        if self.driver.find_element(By.ID,'selected-stop-points-count').is_displayed():
            self.selectPointsButton.click()
            self.selectPointsButton.click()
        else:
            self.selectPointsButton.click()
        self.waitElementDisplayed(self.locators['selectDrawPoints'])
        time.sleep(1)





    # def startTracing(self, tab):
    #     cat = tab.call_method('Tracing.getCategories')
    #     categories = '-*,blink.console,blink.user_timing,devtools.timeline,disabled-by-default-devtools.screenshot,disabled-by-default-devtools.timeline,disabled-by-default-devtools.timeline.invalidationTracking,disabled-by-default-devtools.timeline.frame,disabled-by-default-devtools.timeline.stack,disabled-by-default-v8.cpu_profiler,disabled-by-default-v8.cpu_profiler.hires,latencyInfo,loading,disabled-by-default-lighthouse,v8.execute,v8'
    #     tab.call_method('Network.enable')
    #     tab.call_method('Page.enable')
    #     tab.call_method('Tracing.start', bufferUsageReportingInterval=500, transferMode="ReportEvents",
    #                     categories=categories)

    def stopTracing(self, tab,fileName):
        tab.set_listener('Tracing.tracingComplete', self.output_on_start)
        tab.set_listener('Tracing.dataCollected', self.output_on_end)
        tab.call_method('Tracing.end')
        sleep(10)
        json_object = json.dumps(arrayLog)
        logFileName = datetime.now().strftime(fileName+'_%H_%M_%d_%m_%Y.json')
        # sleep(5)
        with open(r"Logs\ " + logFileName, "a") as outfile:
            outfile.write(json_object)

    def stopTracingEditLogfile(self, tab, fileName):
        tab.set_listener('Tracing.tracingComplete', self.output_on_start)
        tab.set_listener('Tracing.dataCollected', self.output_on_end)
        tab.call_method('Tracing.end')
        sleep(10)
        json_object = json.dumps(arrayLog)
        logFileName = datetime.now().strftime(fileName + '_%H_%M_%d_%m_%Y.json')
        # sleep(5)
        with open(r"Logs\ " + logFileName, "a") as outfile:
            outfile.write(json_object)
        f = open(r"Logs\ " + logFileName)
        data = json.load(f)
        for entry in data:
            for line in entry['value']:
                print("Df")
                # 3 IDI WS TWRA (PWS PAIRNW APO TO KATHENA? FTIAXNW RULES ANALOGWS ME TO CAT ISWS?
                # PWS KSERW OTI DN THA XASW KATI?
                # name functionCall? WHO CARES (EKTOS AN ETSI VLEPW OTI EXEI DATA?
                #

                # {'args': {}, 'cat': 'disabled-by-default-devtools.timeline', 'dur': 20, 'name': 'RunTask', 'ph': 'X',
                #  'pid': 11924, 'tdur': 19, 'tid': 3708, 'ts': 4074249792, 'tts': 527237}

                # {"args": {"data": {"columnNumber": 44, "frame": "08B51E00E6DFA06B1C5CB00846F329C0",
                #                    "functionName": "globalZoneAwareCallback", "lineNumber": 2271, "scriptId": "1369",
                #                    "url": "http://localhost/polyfills.js"}}, "cat": "devtools.timeline", "dur": 1142,
                #  "name": "FunctionCall", "ph": "X", "pid": 18716, "tdur": 808, "tid": 8772, "ts": 102559055674,
                #  "tts": 97564875},

                # {"args": {"data": {"frame": "08B51E00E6DFA06B1C5CB00846F329C0", "id": 2689}},
                #  "cat": "devtools.timeline", "dur": 5133, "name": "FireAnimationFrame", "ph": "X", "pid": 18716,
                #  "tdur": 4246, "tid": 8772, "ts": 102559059380, "tts": 97567836},

                # {"args": {"frameSeqId": 1134212, "layerTreeId": 1},
                #  "cat": "disabled-by-default-devtools.timeline.frame", "name": "DrawFrame", "ph": "I", "pid": 18716,
                #  "s": "t", "tid": 21680, "ts": 102559122988, "tts": 9162862},

                # THELW PITHANON

                # ELEGXW ME CAT GIA NA PARW DIAFORETIKES PERIPTWSEIS?

                # functionName:globalAware
                # dur:
                # name:
                # ts :The tracing clock timestamp of the event. The timestamps are provided at microsecond granularity.
                # tts: The thread clock timestamp of the event. The timestamps are provided at microsecond granularity.
                for value in line['args']:
                    la = value
                    break
                break
            break







    def scrollScaleTimes(self, scale, times):
        actions = ActionChains(self.driver)
        iframe = self.driver.find_element(By.ID, "map")
        scroll_origin = ScrollOrigin.from_element(iframe)
        action=ActionChains(self.driver).context_click()

        for i in range(0, int(times)):
            for i in range(0, int(scale)):
                ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, -400).perform()
                time.sleep(0.5)
            for i in range(0, int(scale)):
                ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, 400).perform()
                time.sleep(0.5)
            # self.driver.execute_script("window.scrollBy(0,250)")
            #
            # actions.key_up(Keys.CONTROL, self.map).perform()
            # actions.key_down(Keys.CONTROL, self.map).perform()
            # self.map.send_keys("-")
            # actions.key_up(Keys.CONTROL, self.map).perform()
            #
            # self.driver.execute_script(("window.scrollTo(0, 3)"))
            # actions.key_up(Keys.CONTROL, self.map)

    # win = self.driver.find_element_by_id("map")
    #         win.send_keys(Keys. + "-")
