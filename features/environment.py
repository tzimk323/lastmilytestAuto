import json
import os
from datetime import datetime
from sys import platform
import sys
import allure
import pychrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Utilities import configReader
# import configReader

headless = configReader.readConfig('automationParams', 'headless')
resolution=configReader.readConfig('automationParams', 'default_resolution')

def before_all(context):
    # Tags dependence
    if 'linux' in platform:
        context.env ='linux'
        print("linux environment")
    elif 'win' in platform:
        context.env = 'windows'
        print("windows environment")

def after_all(context):
    # Tags dependence
    print("Testing over!!")
def before_scenario(context, driver):
    chrome_options = webdriver.ChromeOptions()
    if headless == 'True':
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--enable-logging=stderr')
    chrome_options.add_argument('--enable-precise-memory-info')
    chrome_options.add_argument('--debug-devtools')
    chrome_options.add_argument('--devtools-code-coverage')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_argument('--enable-performance-logging')
    chrome_options.add_argument('--enable-ui-devtools=9223')
    performance_logging = {
        "enableNetwork": True,
        "enablePage": True,
        "traceCategories": 'devtools.timeline'
    }
    caps = DesiredCapabilities.CHROME
    # as per latest docs
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    chrome_options.add_experimental_option("prefs", performance_logging)
    chrome_options.add_experimental_option("detach", True)





    if 'nofe' not in context.tags:
        if context.env=='windows':
            path=ChromeDriverManager().install()
        elif context.env == 'linux':
            path=configReader.readConfig(context.env, 'path')
        context.driver = webdriver.Chrome(executable_path=path, options=chrome_options,desired_capabilities=caps)

    if 'performance' in context.tags:
        dev_tools = pychrome.Browser(url="http://localhost:9222")
        tab = dev_tools.list_tab()[0]
        context.tab=tab
        context.tab.start()

    # context.driver.get('https://beta.lastmily.com/')
    os.system("set PYTHONIOENCODING=utf-8")
    os.system("chcp 65001")
    sys.getdefaultencoding()





def after_scenario(context, driver):
    context.driver.close()
    context.driver.quit()



def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
