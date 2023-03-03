import time
import unittest
from unittest import TestCase

from behave import *

from features.pageobjects.ProjectDaysPage import ProjectDaysPage
from features.pageobjects.ProjectViewPage import ProjectViewPage


@when("I select project day with name '{projectDay}'")
def iSelectProjectDayWithName(context, projectDay):
    ProjectDaysPage(context.driver).ichooseProjectDayWithTitle(projectDay)
    ProjectViewPage(context.driver).waitPageVisible()

@when("I click to create a new project day button")
def iSelectProjectDayWithName(context):
    ProjectDaysPage(context.driver).clickNewProjectDayButton()
    ProjectDaysPage(context.driver).waitNewDayModalVisible()


@when("I set new day title to be '{name}'")
def iSetNewDayTitleToBe(context,name):
    ProjectDaysPage(context.driver).setNewDayTile(name)


@when("I click in new day modal the confirm button")
def iSetNewDayTitleToBe(context):
    ProjectDaysPage(context.driver).clickNewDayModalGoBUtton()
    ProjectViewPage(context.driver).waitPageVisible()




# @Given("Verify that the project day with name '{projectDay}' has the following details:")
# def verifyThatTheProjectDayWithNameHasTHeFollowingDetails(context, projectDay):
#      print("FD")
#      for row in context.table:
#           print(name=row['name'], department=row['department'])
#      ProjectDaysPage(context.driver).ichooseProjectDayWithTitle(projectDay)
#      ProjectViewPage(context.driver).waitPageVisible()
#
#

@then("Verify that the project day with name '{projectDay}' has the following details")
def verifyThatTheProjectDayWithNameHasTheFollowingDetails(context, projectDay):
    model = getattr(context, "model", None)
    arrayActual = []
    arrayExpected = []
    for row in context.table:
        arrayExpected.append(row['Value'])
    arrayActual = ProjectDaysPage(context.driver).getTitlesAndCellDetailsWithTitle(projectDay)
    TestCase().assertListEqual(arrayActual, arrayExpected)

# @then("Verify that the project day with name '{projectDay}' has the following details:")
# def step_impl(context,projectDay):
#    model = getattr(context, "model", None)
#    #iterate rows of table
# @given('Collection of credentials')
# def step_impl(context):
#    model = getattr(context, "model", None)

# @given("Verify that the project day with name '{projectDay}' has the following details:")
# def step_impl(context,projectDay):
#      print("FD")
#      """
#      :type context: behave.runner.Context
#      """
# raise NotImplementedError(
#      u'STEP: Given Verify that the project day with name \'04-01-23\' has the following details:
#      | Stops | 213 |
#      | Drivers | 8 |
#      | Status | Dispatched
# Optimized | ')
