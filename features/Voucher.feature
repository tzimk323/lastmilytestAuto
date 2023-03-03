# -*- coding: utf-8 -*-
Feature: Registration Feature


  @testId-33 @pass @db
  Scenario: Register Automation with email bug
    Given I navigate at lastmily login page 'http://localhost'
#    When I delete from database the following email 'lap36@gmail.com'
    When I click register button
    When I fill register form with following details and register mail
      | Field        | Value      |
      | name         | Theohar    |
      | company name | random     |
      | email        | random     |
      | pass         | 1234       |
      | phone        | 6973483762 |

    Then I click in register page go button
    Then I refresh the page
    Then I click in register page the login link
    When I fill login page username field with previously registered email
    When I fill login page password field with '1234'
    When I click the login button to go to register initialization page


    ##########################  Pass wizard  ##########################
    Then Verify register initialization page options are displayed
    When I click register initialization page start company button
    When I click wizard page set company button
    When I change company with name 'random' to have voucher rights

    When I fill wizard pages with my default values

##########################  Create Time zone ##########################


    When I choose from navbar settings page button
    When I click to navigate to setting options charges
    When I click to new zone charges button
    When I set name at zone charges modal to be 'testCharge'

    When I click to create new weight charge with details
      | Field       | Value |
      | Amount From | Έως   |
      | Amount      | 4     |
      | Type        | Κιλά  |
      | Number      | 3     |

    When I click zone charges charges page submit button

 ##########################  Create Collaborator ##########################
    When I choose from navbar collaborator page button
    When I click new collaborator button
    When I fill new Collaborators form with the following details
      | Field                      | Value               |
      | collaborator name          | Κύριος Collaborator |
      | collaborator address       | click               |
      | collaborator depot address | click               |
      | collaborator mail          | random              |
      | collaborator taxid         | 777777777           |
      | collaborator tax office    | B Αθηνών            |
    When I click new collaborator modal submit button

 ##########################  Create Partner ##########################
    When I choose from navbar partners button
    When I click new partner button
    When I fill new partners form with the following details
      | Field              | Value             |
      | Partner name       | Κύριος Συνεργάτης |
      | Partner address    | click             |
      | Partner mail       | random            |
      | Partner taxid      | 456565656         |
      | Partner tax office | Γ Αθηνών          |
    When I click new partner modal submit button

##########################  Create customer##########################
    When I choose from navbar customers page button
    When I click new customer button
    When I fill new customer form with the following details
      | Field         | Value          |
      | customer name | Κύριος Χρήστος |
      | Phone number  | 1234567891     |
      | address       | click          |


    When I click new customer modal submit button

##########################  choose project  day ##########################
    When I choose from navbar project page button
    When I select the first project on the list
    When I click to create a new project day button
    When I set new day title to be 'firstDay'
    When I click in new day modal the confirm button
    When I click create new stop point button

########################## VOUCHER CREATE AND SUBMIT ##########################
    When I create voucher with the following details
      | Field             | Value               |
      | collaborator type | Company             |
      | By order          | True                |
      | Without delivery  | True                |
      | cosignor name     | Κύριος Collaborator |
      | collaborator name | Κύριος Collaborator |
      | recipient name    | Κύριος Collaborator |
      | recipient address | click               |
      | delivery type     | same day            |
      | charges type      | Αποστολέας          |
      | charges amount    | 10                  |


    When I choose on voucher page submit button
