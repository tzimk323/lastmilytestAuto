import time

from behave import *
from Utilities import configReader
from features.pageobjects.CollaboratorPartnerView import CollaboratorPartnerView
from features.pageobjects.CollaboratorsPage import CollaboratorsPage
from features.pageobjects.CommonFunctions import CommonFunctions
from features.pageobjects.CustomersPage import CustomersPage
from features.pageobjects.DashboardPage import DashboardPage
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.Navbar import Navbar
from features.pageobjects.PartnersPage import PartnersPage
from features.pageobjects.ProjectsPage import ProjectsPage
from features.pageobjects.SettingPage import SettingsPage


@when("I click new collaborator button")
def iClickNewCollaboratorButton(context):
    CollaboratorsPage(context.driver).iClickNewCollaboratorsButton()
    CollaboratorsPage(context.driver).waitNewCollaboratorModalVisible()


@when("I choose in collaborators page the collaborator with name '{name}'")
def iCLickFromcollaboratorPageCollaboratorWithName(context, name):
    if name == 'random':
        name = context.company_name
    CollaboratorsPage(context.driver).chooseCollaboratorWithName(name)
    time.sleep(2)
    # CollaboratorPartnerView(context.driver).waitCollaboratorPartnerPageVisible()


@when("I fill new Collaborators form with the following details")
def iFillNewCollaboratorsFormWithTheFollowingDetails(context):
    CollaboratorsPage(context.driver).iSetNewCollaboratorsNameToBe(context.table[0]['Value'])
    if (context.table[1]['Value'] == 'click'):
        CollaboratorsPage(context.driver).iSetNewCollaboratorsAddressByClickingOnMap()
    else:
        CollaboratorsPage(context.driver).iSetNewCollaboratorsAddressTobe(context.table[1]['Value'])

    if (context.table[2]['Value'] == 'click'):
        CollaboratorsPage(context.driver).iSetNewCollaboratorsDepotAddressByClickingOnMap()
    else:
        CollaboratorsPage(context.driver).iSetNewCollaboratorsDepotAddressTobe(context.table[2]['Value'])

    if (context.table[3]['Value'] == 'senderUsermail'):
        email = configReader.readConfig('MailClientUsers', 'senderUserMail')
    elif (context.table[3]['Value'] == 'random'):
        email = CommonFunctions(context.driver).get_random_string(11) + '@gmail.com'
    else:
        email = context.table[3]['Value']
        context.email = email
    CollaboratorsPage(context.driver).iSetNewCollaboratorsEmailAddressTobe(email)

    CollaboratorsPage(context.driver).iSetNewCollaboratorsTaxIDToBe(context.table[4]['Value'])
    CollaboratorsPage(context.driver).iSetNewCollaboratorsTaxOfficeToBe(context.table[5]['Value'])


@when("I set in new collaborator modal new collaborator name to be '{name}'")
def iSetInNewCollaboratorModalNewPartnerNameToBe(context, name):
    CollaboratorsPage(context.driver).iSetNewCollaboratorsNameToBe(name)


@when("I set in new collaborator modal new collaborator address to be '{address}'")
def iSetInNewCollaboratorModalNewPartnerAddressToBe(context, address):
    CollaboratorsPage(context.driver).iSetNewCollaboratorsAddressTobe(address)


@when("I set in new collaborator modal new email address to be '{address}'")
def iSetInNewcollaboratorModalNewPartnerAddressToBe(context, address):
    CollaboratorsPage(context.driver).iSetNewCollaboratorsEmailAddressTobe(address)


@when("I set in new collaborator modal new collaborator tax id to be '{address}'")
def iSetInNewCollaboratorModalNewPartnerTaxIDToBe(context, address):
    CollaboratorsPage(context.driver).iSetNewCollaboratorsTaxIDToBe(address)


@when("I set in new collaborator modal new collaborator tax office to be '{address}'")
def iSetInNewCollaboratorModalNewCollaboratorTaxOfficeToBe(context, address):
    CollaboratorsPage(context.driver).iSetNewCollaboratorsTaxOfficeToBe(address)


@when("I click new collaborator modal submit button")
def iClickNewCollaboratorModalSubmitButton(context):
    CollaboratorsPage(context.driver).iClickNewCollaboratorsSubmitButton()
    CollaboratorsPage(context.driver).waitNewCollaboratorsModalNOTVisible()
