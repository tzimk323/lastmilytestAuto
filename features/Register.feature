# -*- coding: utf-8 -*-
Feature: Registration Feature

  @pass
  Scenario: 1111111111111111111111
    Given I navigate at lastmily login page 'http://localhost'
    When I delete from database the following email 'lap9@gmail.com'
    When I click register button

#    VOUCHER
#        When I choose on voucher page for collaborator to be an individual radio button
#    When I choose on voucher page for collaborator to be a company radio button
#    When I choose on voucher page for collaborator by order checkbox state to be 'True'
#    When I choose on voucher page for cosignor name to be 'Κύριος Συνεργάτης'
#    When I choose on voucher page for collaborator without delivery checkbox state to be 'True'
#    When I choose on voucher page for collaborator name to be 'Κύριος Collaborator'
#    When I choose on voucher page for recipient name to be 'Kύριος Παραλήπτης'
#    When I choose on voucher page for recipient random address from recipient map
#    When I choose on voucher page for delivery without receipt radio button to be 'True'
#    When I choose on voucher page for delivery next day radio button to be 'True'
#    When I choose on voucher page for delivery same day radio button to be 'True'
#    When I choose on voucher page charges type to be 'Αποστολέας'
#    When I choose on voucher page charges amount of pay to be '10'


#   #   #   #   #   WIZAAAARD #   #   #   #   #   #   #

    #    When I right click on wizard map to choose depot address with coordinates '0' and '0'
#    When I set wizard name of depot to be "the best depot"
#    When I click next wizard button to go to route section
#    When I set to be allowed the slow deliver to 'True'
#    When I set the toggle to be "True" at drivers return for load
#    When I set the slider of time of reloading to be "40"
#    When I click next wizard button to go to delivery section
#    When I set the usual load to be "100"
#    When I set the lastmily access toggle to be "True"
#    When I click next wizard button to go to vehicle section
#    When I choose from wizard page type of vehicle "motor"
#    When I set number of selected vehicles to be "3"
#    When I set maximum load of selected vehicles to be "6000"
#    When I click to add vehicle button
#    When I choose from wizard page type of vehicle "mid-truck"
#    When I set number of selected vehicles to be "2"
#    When I set maximum load of selected vehicles to be "6000"
#    When I click to add vehicle button
#    When I click next wizard button to go to drivers section
#    When I set the maximum driver overtime toggle to be "True"
#    When I click next wizard button to go to drivers settings section
#    When I choose name of driver to be "Giwgos"
#    When I choose phone number of driver to be "random"
#    When I set driver maximum working hours to be "8"
##    TODO:ALMOST RANDOM DRIVER VEHICLE
#    When I choose drivers vehicle ownership from drop down to be "Μηχανάκι"
#    When I click in wizard page the add driver button
#    When I choose name of driver to be "panos"
#    When I choose phone number of driver to be "random"
#    When I set driver maximum working hours to be "9"
#    When I choose drivers vehicle ownership from drop down to be "Μεγάλο Βάν"
#    When I click in wizard page the add driver button
#    When I click wizard finish button

  @testId-33 @pass @db
  Scenario: Register Automation with email bug
    Given I navigate at lastmily login page 'http://localhost'
#    When I delete from database the following email 'lap36@gmail.com'
    When I click register button
    When I fill register form with following details and register mail
      | Field        | Value      |
      | name         | Theohar    |
      | company name | random     |
      | email        | random          |
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


  @collaborator  @testId-34
  Scenario: Register and collaborator creation and register automation
    Given I navigate at lastmily login page 'http://localhost'
#    When I delete from database the following email 'lap34@gmail.com'
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
    When I continue my navigation from the link of the sender email to register
    When I fill register form with following details and register mail
      | Field        | Value         |
      | name         | Collaborator2 |
      | company name | random        |
      | email        | random        |
      | pass         | 1234          |
      | phone        | 6973483762    |

    Then I click in register page go button
    Then I refresh the page
    Then I click in register page the login link
    When I fill login page username field with previously registered email
    When I fill login page password field with '1234'
    When I click the login button


  @partner  @testId-35
  Scenario: Register and partner creation and register automation
    Given I navigate at lastmily login page 'http://localhost'
#    When I delete from database the following email 'lap45@gmail.com'
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
    When I continue my navigation from the link of the sender email to register

    When I fill register form with following details and register mail
      | Field        | Value         |
      | name         | Collaborator2 |
      | company name | random        |
      | email        | random        |
      | pass         | 1234          |
      | phone        | 6973483762    |

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


  @CollaboratorWithVoucher  @testId-36
  Scenario: Register and collaborator creation and register automation
    Given I navigate at lastmily login page 'http://localhost'
#    When I delete from database the following email 'lap47@gmail.com'
#    When I delete from database the following email 'col3@gmail.com'
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
      | delivery type     | next day            |
      | charges type      | Αποστολέας          |
      | charges amount    | 10                  |


    When I choose on voucher page submit button
    When I continue my navigation from the link of the sender email to register
    When I fill register form with following details and register mail
      | Field        | Value         |
      | name         | Collaborator5 |
      | company name | random        |
      | email        | random        |
      | pass         | 1234          |
      | phone        | 6973483762    |

    Then I click in register page go button
    Then I refresh the page
    Then I click in register page the login link
    When I fill login page username field with previously registered email
    When I fill login page password field with '1234'
    When I click the login button


  @PartnerWithVoucherAndRegister @testId-37
  Scenario: Register and parnter creation and register automation for both
    Given I navigate at lastmily login page 'http://localhost'
#    When I delete from database the following email 'lap53@gmail.com'
#    When I delete from database the following email 'parvr6@gmail.com'
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

    When I choose from navbar project page button
    When I select the first project on the list
    When I click to create a new project day button
    When I set new day title to be 'firstDay'
    When I click in new day modal the confirm button
    When I click create new stop point button

########################## VOUCHER CREATE AND SUBMIT ##########################
    When I create voucher with the following details
      | Field             | Value             |
      | collaborator type | Company           |
      | By order          | True              |
      | Without delivery  | True              |
      | cosignor name     | Κύριος Συνεργάτης |
      | collaborator name | Κύριος Συνεργάτης |
      | recipient name    | Κύριος Συνεργάτης |
      | recipient address | click             |
      | delivery type     | next day          |
      | charges type      | Αποστολέας        |
      | charges amount    | 10                |


    When I choose on voucher page submit button
    When I continue my navigation from the link of the sender email to register
    When I fill register form with following details and register mail
      | Field        | Value         |
      | name         | Collaborator5 |
      | company name | random        |
      | email        | random        |
      | pass         | 1234          |
      | phone        | 6973483762    |

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
    When SCENARIO SECTION: 'END'
    When I choose from navbar partners button
    When I click from partner page history of shipments navigation button

    When Verify from shipments history row '1' and column '1' holds the value: 'Κύριος Συνεργάτης - -'
#    When Verify from shipments history row '1' and column '2' holds the value: '21/02/2023'
    When Verify from shipments history row '1' and column '3' holds the value: '340 03 Κύμη Εύβοια'
    When Verify from shipments history row '1' and column '4' holds the value: '- (08:00-20:00)'
    When Verify from shipments history row '1' and column '5' holds the value: '50 10 1'
    When Verify from shipments history row '1' and column '6' holds the value: 'Έχει 10.00€'
    When Verify from shipments history row '1' and column '8' holds the value: 'Μη-Προγραμματισμένο'


  @PartnerWithTimologisi @testID-40 @NOTPASS
  Scenario: Register and partner creation and invoice
    Given I navigate at lastmily login page 'http://localhost'
#    When I delete from database the following email 'tim1@gmail.com'
#    When I delete from database the following email 'partim1@gmail.com'
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

    When I choose from navbar project page button
    When I select the first project on the list
    When I click to create a new project day button
    When I set new day title to be 'firstDay'
    When I click in new day modal the confirm button
    When I click create new stop point button

########################## VOUCHER CREATE AND SUBMIT ##########################
    When I create voucher with the following details
      | Field             | Value             |
      | collaborator type | Company           |
      | By order          | True              |
      | Without delivery  | True              |
      | cosignor name     | Κύριος Συνεργάτης |
      | collaborator name | Κύριος Συνεργάτης |
      | recipient name    | Κύριος Συνεργάτης |
      | recipient address | click             |
      | delivery type     | next day          |
      | charges type      | Αποστολέας        |
      | charges amount    | 10                |


    When I choose on voucher page submit button

    # INVOICE
    When I choose from navbar partners button
    When I click from partner page view partners navigation button
    When I choose in view partner page the partner with name 'Κύριος Συνεργάτης'
    When I choose from collaborator partner view page the stop point nav button
    When I choose from collaborator view page the invoice filter button


    When I continue my navigation from the link of the sender email to register
    When I fill register form with following details and register mail
      | Field        | Value         |
      | name         | Collaborator5 |
      | company name | random        |
      | email        | random        |
      | pass         | 1234          |
      | phone        | 6973483762    |

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
    When SCENARIO SECTION: 'END'
    When I choose from navbar partners button
    When I click from partner page history of shipments navigation button

    When Verify from shipments history row '1' and column '1' holds the value: 'Κύριος Συνεργάτης - SC39174485'
    When Verify from shipments history row '1' and column '2' holds the value: '21/02/2023'
    When Verify from shipments history row '1' and column '3' holds the value: '340 03 Κύμη Εύβοια'
    When Verify from shipments history row '1' and column '4' holds the value: '- (08:00-20:00)'
    When Verify from shipments history row '1' and column '5' holds the value: '50 10 1'


  @CollaboratorWithVoucherANDDInvoice  @testId-46  @bug
  Scenario: Register and collaborator creation register and INVOICE
    Given I navigate at lastmily login page 'http://localhost'
#    When I delete from database the following email 'colabIn@gmail.com'
#    When I delete from database the following email 'mist@gmail.com'
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
      | collaborator name          | Mister Collaborator |
      | collaborator address       | click               |
      | collaborator depot address | click               |
      | collaborator mail          | random              |
      | collaborator taxid         | 777777777           |
      | collaborator tax office    | B Αθηνών            |

    When I click new collaborator modal submit button
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
      | cosignor name     | Mister Collaborator |
      | collaborator name | Mister Collaborator |
      | recipient name    | Mister Collaborator |
      | recipient address | click               |
      | delivery type     | next day            |
      | charges type      | Αποστολέας          |
      | charges amount    | 10                  |


    When I choose on voucher page submit button

        # INVOICE
    When I choose from navbar collaborator page button
    When I choose in collaborators page the collaborator with name 'Mister Collaborator'
    When I choose from collaborator partner view page the stop point nav button partners
    When I choose from collaborator partner view page the manual invoice button

    When I continue my navigation from the link of the sender email to register
    When I fill register form with following details and register mail
      | Field        | Value         |
      | name         | Collaborator5 |
      | company name | random        |
      | email        | random        |
      | pass         | 1234          |
      | phone        | 6973483762    |

    Then I click in register page go button
    Then I refresh the page
    Then I click in register page the login link
    When I fill login page username field with previously registered email
    When I fill login page password field with '1234'
    When I click the login button


  @CollaboratorWithVoucherANDDInvoiceNoReceipt  @testId-49
  Scenario: Register and collaborator creation register and INVOICE no receipt
    Given I navigate at lastmily login page 'http://localhost'
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
      | collaborator name          | Mister Collaborator |
      | collaborator address       | click               |
      | collaborator depot address | click               |
      | collaborator mail          | random              |
      | collaborator taxid         | 777777777           |
      | collaborator tax office    | B Αθηνών            |

    When I click new collaborator modal submit button
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
      | By order          | -                   |
      | Without delivery  | True                |
      | cosignor name     | -                   |
      | collaborator name | Mister Collaborator |
      | recipient name    | exampleName         |
      | recipient address | click               |
      | delivery type     | no delivery         |
      | charges type      | Αποστολέας          |
      | charges amount    | 10                  |


    When I choose on voucher page submit button

        # INVOICE
    When I choose from navbar collaborator page button
    When I choose in collaborators page the collaborator with name 'Mister Collaborator'
    When I choose from collaborator partner view page the stop point nav button partners
    When I choose from collaborator partner view page the manual invoice button
    When I choose to invoice the stop point with address '340 03 Κύμη Εύβοια'
    When I click the invoice button
    Then Verify from invoice at row '1' and column '2' holds the value: 'Δημιουργήθηκε'
    Then Verify from invoice at row '1' and column '5' holds the value: '4.00€'
    Then Verify from invoice at row '1' and column '6' holds the value: 'Έγκριση'
    When I click from the invoice of number '1' the action approved button
    Then Verify from invoice at row '1' and column '2' holds the value: 'Εγκρίθηκε'
    Then Verify from invoice at row '1' and column '6' holds the value: 'Πληρωμή'



    When I continue my navigation from the link of the sender email to register
    When I fill register form with following details and register mail
      | Field        | Value         |
      | name         | Collaborator5 |
      | company name | random2       |
      | email        | random        |
      | pass         | 1234          |
      | phone        | 6973483762    |

    Then I click in register page go button
    Then I refresh the page
    Then I click in register page the login link
    When I fill login page username field with previously registered email
    When I fill login page password field with '1234'
    When I click the login button
    When I choose from collaborator navbar collaborator partner page button
    When I choose in collaborators page the collaborator with name 'random'
    When SCENARIO SECTION: 'here'
    Then Verify from invoice at row '1' and column '3' holds the value: '340 03 Κύμη Εύβοια'
    Then Verify from invoice at row '1' and column '6' holds the value: 'Έχει 10.00€'
    Then Verify from invoice at row '1' and column '7' holds the value: 'Προς πληρωμή'
    Then Verify from invoice at row '1' and column '8' holds the value: 'Μη-Προγραμματισμένο'


 @CollaboratorWithVoucherANDDNotInvoiceNoTReceipt  @testId-89
  Scenario: Register and collaborator creation register and NOT INVOICE no receipt
    Given I navigate at lastmily login page 'http://localhost'
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
      | collaborator name          | Mister Collaborator |
      | collaborator address       | click               |
      | collaborator depot address | click               |
      | collaborator mail          | random              |
      | collaborator taxid         | 777777777           |
      | collaborator tax office    | B Αθηνών            |

    When I click new collaborator modal submit button
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
      | By order          | -                   |
      | Without delivery  | True                |
      | cosignor name     | -                   |
      | collaborator name | Mister Collaborator |
      | recipient name    | exampleName         |
      | recipient address | click               |
      | delivery type     | no delivery         |
      | charges type      | Αποστολέας          |
      | charges amount    | 10                  |


    When I choose on voucher page submit button
    When I continue my navigation from the link of the sender email to register
    When I fill register form with following details and register mail
      | Field        | Value         |
      | name         | Collaborator5 |
      | company name | random2       |
      | email        | random        |
      | pass         | 1234          |
      | phone        | 6973483762    |

    Then I click in register page go button
    Then I refresh the page
    Then I click in register page the login link
    When I fill login page username field with previously registered email
    When I fill login page password field with '1234'
    When I click the login button
    When I choose from collaborator navbar collaborator partner page button
    When I choose in collaborators page the collaborator with name 'random'
    When SCENARIO SECTION: 'here'
    Then Verify from invoice at row '1' and column '3' holds the value: '340 03 Κύμη Εύβοια'
    Then Verify from invoice at row '1' and column '6' holds the value: 'Έχει 10.00€'
    Then Verify from invoice at row '1' and column '7' holds the value: '-'
    Then Verify from invoice at row '1' and column '8' holds the value: 'Μη-Προγραμματισμένο'
  @ththy
  Scenario: Register test
    When I choose in collaborators page the collaborator with name 'Κύριος Collaborator'





