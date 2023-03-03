from behave import *

from features.pageobjects.StopPointPage import StopPointPage


@when("I create voucher with the following details")
def iCreateVoucherWithTheFollowingDetails(context):
    if context.table[0]['Value'].lower() == 'company':
        StopPointPage(context.driver).setRadioValueForCompany(True)
    elif context.table[0]['Value'].lower() == 'individual':
        StopPointPage(context.driver).setRadioValueForPerson(True)
    if context.table[1]['Value'] != '-':
        StopPointPage(context.driver).setValuebyOrderCheckBox(context.table[1]['Value'])
    if context.table[2]['Value'] != '-':
        StopPointPage(context.driver).setWithoutDeliveryCheckbox(context.table[2]['Value'])
    if context.table[3]['Value'] != '-':
        StopPointPage(context.driver).setCosignorNameField(context.table[3]['Value'])
    StopPointPage(context.driver).setVoucherSenderName(context.table[4]['Value'])
    StopPointPage(context.driver).setVoucherReceiverName(context.table[5]['Value'])
    if context.table[6]['Value'] == 'click':
        StopPointPage(context.driver).chooseVoucherReceiverAddressMap()
    else:
        StopPointPage(context.driver).setVoucherReceiverAddress(context.table[6]['Value'])
    if context.table[7]['Value'].lower() == 'same day':
        StopPointPage(context.driver).setSameDayDeliveryRadio(True)
    elif context.table[7]['Value'].lower() == 'next day':
        StopPointPage(context.driver).setNextDayDeliveryRadio(True)
    elif context.table[7]['Value'].lower() == 'no delivery':
        StopPointPage(context.driver).setDeliveryWithoutReceiptRadio(True)
    StopPointPage(context.driver).setVoucherChargesType(context.table[8]['Value'])
    StopPointPage(context.driver).setVoucherPayAmount(context.table[9]['Value'])


@when("I choose on voucher page for collaborator to be an individual radio button")
def iChooseOnVoucherPageForCollaboratorToBeAnIndividualRadioButton(context):
    StopPointPage(context.driver).setRadioValueForPerson(True)


@when("I choose on voucher page for collaborator to be a company radio button")
def iChooseOnVoucherPageForCollaboratorToBeACompanyRadioButton(context):
    StopPointPage(context.driver).setRadioValueForCompany(True)


@when("I choose on voucher page for collaborator by order checkbox state to be '{state}'")
def iChooseOnVoucherPageForCollaboratorByOrderCheckboxStateToBe(context, state):
    StopPointPage(context.driver).setValuebyOrderCheckBox(state)


@when("I choose on voucher page for collaborator without delivery checkbox state to be '{state}'")
def iChooseOnVoucherPageForCollaboratorWithoutDeliveryCheckboxStateToBe(context, state):
    StopPointPage(context.driver).setWithoutDeliveryCheckbox(state)


@when("I choose on voucher page for collaborator name to be '{name}'")
def iChooseOnVoucherPageForCollaboratorNameToBe(context, name):
    StopPointPage(context.driver).setVoucherSenderName(name)


@when("I choose on voucher page for cosignor name to be '{name}'")
def iChooseOnVoucherPageForCosignorNameToBe(context, name):
    StopPointPage(context.driver).setCosignorNameField(name)


@when("I choose on voucher page for recipient name to be '{name}'")
def iChooseOnVoucherPageForRecipientNameToBe(context, name):
    StopPointPage(context.driver).setVoucherReceiverName(name)


@when("I choose on voucher page for recipient address to be '{address}'")
def iChooseOnVoucherPageForRecipientAddressToBe(context, address):
    StopPointPage(context.driver).setVoucherReceiverAddress(address)


@when("I choose on voucher page for recipient random address from recipient map")
def iChooseOnVoucherPageForRecipientAddressToBe(context):
    StopPointPage(context.driver).chooseVoucherReceiverAddressMap()


@when("I choose on voucher page for delivery without receipt radio button to be '{state}'")
def iChooseOnVoucherPageForDeliveryWithoutReceiptRadioButtonToBe(context, state):
    StopPointPage(context.driver).setDeliveryWithoutReceiptRadio(state)


@when("I choose on voucher page for delivery next day radio button to be '{state}'")
def iChooseOnVoucherPageForDeliveryNextDayRadioButtonToBe(context, state):
    StopPointPage(context.driver).setNextDayDeliveryRadio(state)


@when("I choose on voucher page for delivery same day radio button to be '{state}'")
def iChooseOnVoucherPageForDeliverySameDayRadioButtonToBe(context, state):
    StopPointPage(context.driver).setSameDayDeliveryRadio(state)


@when("I choose on voucher page charges type to be '{type}'")
def iChooseOnVoucherPageChargesTypeToBe(context, type):
    StopPointPage(context.driver).setVoucherChargesType(type)


@when("I choose on voucher page charges amount of pay to be '{amount}'")
def iChooseOnVoucherPageChargesAmountOfPayToBe(context, amount):
    StopPointPage(context.driver).setVoucherPayAmount(amount)


@when("I choose on voucher page submit button")
def iChooseOnVoucherPageSubmitButton(context):
    StopPointPage(context.driver).iClickVoucherSubmitButton()
    StopPointPage(context.driver).waitPageNotVisible()
