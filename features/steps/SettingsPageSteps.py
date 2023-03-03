import time

from behave import *
from Utilities import configReader
from features.pageobjects.DashboardPage import DashboardPage
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.Navbar import Navbar
from features.pageobjects.ProjectsPage import ProjectsPage
from features.pageobjects.SettingPage import SettingsPage
from features.pageobjects.ZoneChargesPage import ZoneChargesPage


@when("I scroll to the time windows section")
def iScrollToTheTimeWindowsSection(context):
    SettingsPage(context.driver).scrollIntoViewToSection('time windows')

@when("I scroll to the charges section")
def iScrollToTheTimeWindowsSection(context):
    SettingsPage(context.driver).scrollIntoViewToSection('charges')

@when("I click to navigate to setting options charges")
def iClickToNavigateToSettingsOptionsCharges(context):
    SettingsPage(context.driver).clickInsettingsMenuToVisitSection('charges')

@when("I click to new zone charges button")
def iClickZoneChargesButton(context):
    SettingsPage(context.driver).clickNewZoneChargesButton()
    ZoneChargesPage(context.driver).waitPageVisible()

@when("I click to navigate to setting options time windows")
def iClickToNavigateToSettingsOptionsTimeWindows(context):
    SettingsPage(context.driver).clickInsettingsMenuToVisitSection('time-windows')

@when("V")
def iClickToNavigateToSettingsOptionsTimeWindows(context):
    SettingsPage(context.driver).clickInsettingsMenuToVisitSection('time-windows')