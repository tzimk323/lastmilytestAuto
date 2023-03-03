import time
from unittest import TestCase

from behave import *
from Utilities import configReader

from features.pageobjects.DashboardPage import DashboardPage
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.ProjectsPage import ProjectsPage
from features.pageobjects.RegisterInitPage import RegisterInitPage
from features.pageobjects.RegisterPage import RegisterPage
from features.pageobjects.WizardPage import WizardPage


@then("Verify register initialization page options are displayed")
def verifyRegisterInitializationPageOptionsAreDisplayed(context):
    context.registerInit = RegisterInitPage(context.driver)
    TestCase().assertTrue(context.registerInit.isStartCompanyButtonDisplayed(), "register initialization page start company button is NOT displayed")
    TestCase().assertTrue(context.registerInit.isStartDemoButtonDisplayed(), "register initialization page start demo button is NOT displayed")


@when("I click register initialization page start company button")
def iClickRegisterInitializationPageStartCompanyButton(context):
    context.registerInit = RegisterInitPage(context.driver)
    context.registerInit.clickstartCompanyButton()
    context.wizard= WizardPage(context.driver).waitPageVisible()


