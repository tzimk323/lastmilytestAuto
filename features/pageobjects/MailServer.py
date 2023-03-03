from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from Utilities import configReader
from features.pageobjects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
from seleniumpagefactory import PageFactory
import abc
import unittest
import mailslurp_client


class MailServer:

    def returnLinkFromEmail(user):
        if (user == 'sender' or user == 'senderRegister'):
            apiKey = configReader.readConfig('MailClientUsers', 'mailSenderApikey')
            emailId = configReader.readConfig('MailClientUsers', 'mailSlurpSenderID')
        elif (user == 'register'):
            apiKey = configReader.readConfig('MailClientUsers', 'mailSlurpApikey')
            emailId = configReader.readConfig('MailClientUsers', 'mailSlurpMailID')
        elif (user == 'sender2' or user == 'senderRegister2'):
            apiKey = configReader.readConfig('MailClientUsers', 'mailSecondSenderApikey')
            emailId = configReader.readConfig('MailClientUsers', 'mailSlurpSecondSenderID')

        config = mailslurp_client.Configuration()
        config.api_key['x-api-key'] = apiKey

        email = mailslurp_client.WaitForControllerApi(config).wait_for_latest_email(inbox_id=emailId, timeout=30000,
                                                                                    unread_only=True)

        if (user == 'senderRegister' or user == 'senderRegister2'):
            finalLink = "http" + email.body.split("http")[1].split("<")[0]
        else:
            finalLink = email.body.split("href=")[1].split(">")[0].replace('"', '')

        return finalLink
