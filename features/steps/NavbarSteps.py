import time

from behave import *
from Utilities import configReader
from features.pageobjects.CollaboratorPartnerView import CollaboratorPartnerView
from features.pageobjects.CollaboratorsPage import CollaboratorsPage
from features.pageobjects.CustomersPage import CustomersPage
from features.pageobjects.DashboardPage import DashboardPage
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.Navbar import Navbar
from features.pageobjects.PartnersPage import PartnersPage
from features.pageobjects.ProjectsPage import ProjectsPage
from features.pageobjects.SettingPage import SettingsPage


@when("I choose from navbar project page button")
def iChooseFromNavarProjectPageButton(context):
    context.nav = Navbar(context.driver).clickProjectButton()
    ProjectsPage(context.driver).waitPageVisible()

@when("I choose from navbar settings page button")
def iChooseFromNavarSettingsPageButton(context):
    context.nav = Navbar(context.driver).clickSettingsPageButton()
    SettingsPage(context.driver).waitPageVisible()

@when("I choose from navbar partners button")
def iChooseFromNavbarParntersPageButton(context):
    context.nav = Navbar(context.driver).clickPartnersPageButton()
    PartnersPage(context.driver).waitPageVisible()

@when("I choose from navbar collaborator page button")
def iChooseFromNavbarCollaboratorPageButton(context):
    context.nav = Navbar(context.driver).clickCollaboratorsPageButton()
    CollaboratorsPage(context.driver).waitPageVisible()


@when("I choose from navbar customers page button")
def iChooseFromNavbarCoustomersPageButton(context):
    context.nav = Navbar(context.driver).clickCustomersPageButton()
    CustomersPage(context.driver).waitPageVisible()

@when("I choose from navbar senders button")
def iChooseFromNavbarSendersPageButton(context):
    context.nav = Navbar(context.driver).clickSendersPageButton()
    # ProjectsPage(context.driver).waitPageVisible()



@when("I choose from collaborator navbar collaborator partner page button")
def iChooseFromCollaboratorNavbarCollaboratorPartnerPageButton(context):
    context.nav = Navbar(context.driver).clickCollaboratorsPartnersPageButton()
    time.sleep(2)
