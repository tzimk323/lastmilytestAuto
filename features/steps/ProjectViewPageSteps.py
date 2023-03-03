import time

from behave import *

from Utilities import configReader
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.ProjectDaysPage import ProjectDaysPage
from features.pageobjects.ProjectViewPage import ProjectViewPage
import unittest
from unittest import TestCase

from features.pageobjects.StopPointPage import StopPointPage


@when("I click on map at point with offset x: '{x}' and y: '{y}'")
def iClickOnMapAtPointWithAnd(context, x, y):
    context.ProjectView = ProjectViewPage(context.driver)
    context.ProjectView.clickOnMapWithOffset(x, y)


@when("I hover on map with offset x: '{x}' and y: '{y}'")
def iClickOnMapAtPointWithAnd(context, x, y):
    context.ProjectView = ProjectViewPage(context.driver)
    context.ProjectView.hoverOnMapWithOffset(x, y)


@then("Verify vehicle hover box is opened with name '{name}'")
def verifyVehicleHoverBoxIsOpenedWithName(context, name):
    context.ProjectView = ProjectViewPage(context.driver)
    result = context.ProjectView.isVehicleHoverBoxVisible()
    resultText = context.ProjectView.getVehicleHoverBoxTitle()
    TestCase().assertTrue(result, "Hover box of vihicle should be diplayed")
    TestCase().assertEqual(resultText, name, "Vehicle box name should be: " + name + " but instead is: " + resultText)


@then("Verify vehicle hover box is opened with last seen status '{name}'")
def verifyVehicleHoverBoxIsOpenedWithLastSeenStatus(context, name):
    context.ProjectView = ProjectViewPage(context.driver)
    result = context.ProjectView.isVehicleHoverBoxVisible()
    resultText = context.ProjectView.getVehicleHoverBoxLastSeenText()
    TestCase().assertTrue(result, "Hover box of vihicle should be diplayed")
    TestCase().assertEqual(resultText, name,
                           "Vehicle box last seen should be: " + name + " but instead is: " + resultText)


@then("Verify stop point hover box is opened with name '{name}'")
def verifyStopPointHoverBoxIsOpenedWithName(context, name):
    context.ProjectView = ProjectViewPage(context.driver)
    result = context.ProjectView.isStopPointHoverBoxVisible()
    resultText = context.ProjectView.getStopPointHoverBoxTitle()
    TestCase().assertTrue(result, "Hover box of stop point should be diplayed")
    TestCase().assertTrue(resultText == name, "Vehicle box name should be: " + name + " but instead is: " + resultText)


@when("I right click on map at point with offset x: '{x}' and y: '{y}'")
def iClickOnMapAtPointWithAnd(context, x, y):
    context.ProjectView = ProjectViewPage(context.driver)
    context.ProjectView.rightclickOnMapWithOffset(x, y)


@when("I right click on sp at point with offset x: '{x}' and y: '{y}' and wait keep time until windows opens")
def iRightClickOnSpWithOffsetAndKeepWaitUntilChoicesWindowOpen(context, x, y):
    context.ProjectView = ProjectViewPage(context.driver)
    context.time = context.ProjectView.rightclickOnSpWithOffsetAndKeepTime(x, y)


@when("I click back button")
def iClickBackButton(context):
    context.ProjectView = ProjectViewPage(context.driver)
    context.ProjectView.iClickTheBackButton()
    ProjectDaysPage(context.driver).waitPageVisible()


@when("I click and the papaki to trigger refresh/update a request")
def iClickOnTheMiddleBarSectionToTriggerARefreshUpdateRequest(context):
    context.ProjectView = ProjectViewPage(context.driver)
    context.ProjectView.clickAtPapakiSymbol()
    context.ProjectView.waitRequestBarAppear()


@when("I choose from the stop point right click choices to '{choice}'")
def iChooseFromTHeStopPointRightClickChoicesTo(context, choice):
    context.ProjectView = ProjectViewPage(context.driver)
    context.ProjectView.chooseDisableStopPoint(choice)


@when("I choose from the stop point right click choices to change state of points")
def iChooseFromTHeStopPointRightClickChoicesToChangeStateOfPoints(context):
    context.ProjectView = ProjectViewPage(context.driver)
    context.ProjectView.changeStateOfStopPoint()


@when("I click create new stop point button")
def iClickCreateNewStopPointButton(context):
    ProjectViewPage(context.driver).clickCreateNewStopButton()
    StopPointPage(context.driver).waitPageVisible()


@when("I choose from the stop point right click choices to change priority of points")
def iChooseFromTHeStopPointRightClickChoicesToChangeStateOfPoints(context):
    context.ProjectView = ProjectViewPage(context.driver)
    context.ProjectView.changePriorityOfStopPoint()


#
# @when("I click on map at point with 'x' and 'y'")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: When I click on map at point with \'x\' and \'y\'')
@when("I scroll zoomin and zoom out at scales '{scale}' for '{times}' times")
def iScrollZoominAndZoomOutAtScales(context, scale, times):
    context.ProjectView = ProjectViewPage(context.driver)
    context.ProjectView.scrollScaleTimes(scale, times)


@when("I click select points button to show options")
def iClickSelectPointsButtonToShowOptions(context):
    context.ProjectView = ProjectViewPage(context.driver)
    context.ProjectView.clickSelectPointsButtonToShowOptions()


@when("I click draw points button")
def iClickSelectPointsButton(context):
    context.ProjectView = ProjectViewPage(context.driver)
    context.ProjectView.clickDrawPointsButton()


@when("I scroll zoomin and zoom out at scales '{scale}' for '{times}' times at point of map with x '{x}' and y '{y}'")
def iScrollZoominAndZoomOutAtScales(context, scale, times, x, y):
    context.ProjectView = ProjectViewPage(context.driver)
    context.ProjectView.clickOnMapWithOffsetAndZoomAtScaleAndTimes(x, y, times, scale)
