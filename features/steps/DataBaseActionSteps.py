import time

from behave import *
from Utilities import configReader
from features.pageobjects.DashboardPage import DashboardPage
from features.pageobjects.DatabaseActions import DatabaseActions
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.Navbar import Navbar
from features.pageobjects.ProjectsPage import ProjectsPage


@when("I delete from database the following email '{email}'")
def iDeleteFromDataBaseTheFollowingEmail(context, email):
    DatabaseActions().deleteTheEmail(email)


@when("I get from database the collaborator invite link")
def iGetFromDatabaseTheCollaboratorInviteLink(context):
    DatabaseActions().deleteTheEmail()


@when("I drop default lastmily database")
def iDropDefaultLastMilyDatabase(context):
    DatabaseActions().deletedatase()


@when("I drop lastmily database with name '{dbname}'")
def iDropDefaultLastMilyDatabase(context,dbname):
    DatabaseActions().deletedatase(dbname)

# @when("I upload database with name '{dbname}'")
# def iUploadDatabaseWithName(context,dbname):
#     DatabaseActions()(dbname)



@when("I create new database with name '{dbname}'")
def iCreateNewDatabaseWithName(context, dbname):
    DatabaseActions().createDatabase(dbname)

@when("I dump my database")
def iCreateNewDatabaseWithName(context):
    DatabaseActions().dumpMydatabase()


@when("I create new database with default name")
def iCreateNewDatabaseDefault(context):
    DatabaseActions().createDatabase()

@when("I create a backup database")
def iCreateBackupDatabase(context):
    DatabaseActions().createBackupDatabaseDump()



@when("I change company with name '{name}' to have voucher rights")
def iChangeCompanyWithNameToHaveVoucherRights(context, name):
    if name.lower() == 'random':
        name=context.company_name
    DatabaseActions().changeCompanyTohaveVoucher(name)
    print("The random company name is: " + name)
    print("The email used is: " + context.email)
