@performance
Feature: Registration Feature

  @pass   @reggression  @database
  Scenario: simple zoom in/out in not optimized PP
    Given I navigate at lastmily login page 'https://beta.lastmily.com/'
    When I fill login page username field with 'd.s.konstant@gmail.com'
    When I fill login page password field with '1234'
    When I click the login button
    When I choose from navbar project page button
    When I select project with name 'first project'
    Then Verify that the project day with name 'ghghg' has the following details
     | Title    | Value                        |
     | Dep Time | 08:10                        |
     | Distance |                              |
     | Stops    | 11                           |
     | Drivers  | 0                            |
     | Status   | Un-Dispatched Initialization |

    When I select project day with name 'ghghg'
    When I start performance tracing with dev tools
    When I click on map at point with offset x: '200' and y: '200'
    When I scroll zoomin and zoom out at scales '5' for '5' times
    When I stop performance tracing with dev tools and i save the file to 'FirstTest19'


  @emulationCpu10 @pass
  Scenario: EMULATION : SLOW CPU,simple zoom in/out in not optimized PP
    Given I navigate at lastmily login page 'https://beta.lastmily.com/'
    When I fill login page username field with 'd.s.konstant@gmail.com'
    When I fill login page password field with '1234'
    When I click the login button
    When I choose from navbar project page button
    When I select project with name 'first project'
    Then Verify that the project day with name 'ghghg' has the following details
      | Title    | Value                        |
      | Dep Time | 08:10                        |
      | Distance |                              |
      | Stops    | 11                           |
      | Drivers  | 0                            |
      | Status   | Un-Dispatched Initialization |
    When I select project day with name 'ghghg'
    When I send command via CDP to emulate a cpu with throttling rate of '10'
    When I start performance tracing with dev tools
    When I scroll zoomin and zoom out at scales '3' for '3' times
    When I stop performance tracing with dev tools and i save the file to 'FirstTest'


 @Pass @scrollFails
  Scenario: simple zoom in/out in optimized and dispatched PP with driver tracking (1-50 drivers ?)
    Given I navigate at lastmily login page 'https://dev2.lastmily.com/'
    When I fill login page username field with 'jim@lastmily.com'
    When I fill login page password field with 'asdf'
    When I click the login button
    When I choose from navbar project page button
    When I select project with name 'Dianomi'
   Then Verify that the project day with name '04-01-23' has the following details
     | Title    | Value                |
     | Dep Time | 06:30                |
     | Distance | 1723.01km            |
     | Stops    | 213                  |
     | Drivers  | 8                    |
     | Status   | Re-Dispatch Optimized |
    When I select project day with name '04-01-23'
    When I start performance tracing with dev tools
    When I scroll zoomin and zoom out at scales '5' for '5' times
    When I stop performance tracing with dev tools and i save the file to 'test2'


  @Pass @need2More
  Scenario: load a PP with many (over 1000) stop points, optimized and initialization state, dispatched and undispatched (ZOOM IN ZOOM OUT)
    Given I navigate at lastmily login page 'https://dev2.lastmily.com/'
    When I fill login page username field with 'ups_thanos@lastmily.com'
    When I fill login page password field with '1234'
    When I click the login button
    When I choose from navbar project page button
    When I select project with name '1st project'
    Then Verify that the project day with name 'odiko + aeroporiko (6 lepta)' has the following details
      | Title    | Value                |
      | Dep Time | 09:30                |
      | Distance | 1510.01km            |
      | Stops    | 1327                 |
      | Drivers  | 17                   |
      | Status   | Dispatched Optimized |

    When I select project day with name 'odiko + aeroporiko (6 lepta)'
    When I start performance tracing with dev tools
    When I scroll zoomin and zoom out at scales '5' for '5' times
    When I stop performance tracing with dev tools and i save the file to 'test2'


  @pass @itAlwaysHoverONCenterWatchout
  Scenario: Polygon select stop points and changing them to priority/disabled
    Given I navigate at lastmily login page 'https://dev2.lastmily.com/'
    When I fill login page username field with 'jim@lastmily.com'
    When I fill login page password field with 'asdf'
    When I click the login button
    When I choose from navbar project page button
    When I select project with name 'Dianomi'
    Then Verify that the project day with name '04-01-23' has the following details
     | Title    | Value                 |
     | Dep Time | 06:30                 |
     | Distance | 1723.01km             |
     | Stops    | 213                   |
     | Drivers  | 8                     |
     | Status   | Re-Dispatch Optimized |

    When I select project day with name '04-01-23'
    When I start performance tracing with dev tools
    When I click select points button to show options
    When I click draw points button
    When I click on map at point with offset x: '200' and y: '200'
    When I click on map at point with offset x: '-200' and y: '200'
    When I click on map at point with offset x: '-50' and y: '-250'
    When I click on map at point with offset x: '200' and y: '200'
    When I right click on map at point with offset x: '200' and y: '200'
    When I choose from the stop point right click choices to change state of points
    When I click select points button to show options
    When I click draw points button
    When I click on map at point with offset x: '200' and y: '200'
    When I click on map at point with offset x: '-200' and y: '200'
    When I click on map at point with offset x: '-50' and y: '-250'
    When I click on map at point with offset x: '200' and y: '200'
    When I right click on map at point with offset x: '200' and y: '200'
    When I choose from the stop point right click choices to change state of points
    When I click select points button to show options
    When I click draw points button
    When I click on map at point with offset x: '200' and y: '200'
    When I click on map at point with offset x: '-200' and y: '200'
    When I click on map at point with offset x: '-50' and y: '-250'
    When I click on map at point with offset x: '200' and y: '200'
    When I right click on map at point with offset x: '200' and y: '200'
    When I choose from the stop point right click choices to change priority of points
    When I click select points button to show options
    When I click draw points button
    When I click on map at point with offset x: '200' and y: '200'
    When I click on map at point with offset x: '-200' and y: '200'
    When I click on map at point with offset x: '-50' and y: '-250'
    When I click on map at point with offset x: '200' and y: '200'
    When I right click on map at point with offset x: '200' and y: '200'
    When I choose from the stop point right click choices to change priority of points
    When I stop performance tracing with dev tools and i save the file to 'FirstTest'


  @pass
  Scenario:while a request is pending (eg tracking request) make a SP priority/disabled
    Given I navigate at lastmily login page 'https://dev2.lastmily.com/'
    When I fill login page username field with 'jim@lastmily.com'
    When I fill login page password field with 'asdf'
    When I click the login button
    When I choose from navbar project page button
    When I select project with name 'Dianomi'
    Then Verify that the project day with name '04-01-23' has the following details
     | Title    | Value                 |
     | Dep Time | 06:30                 |
     | Distance | 1723.01km             |
     | Stops    | 213                   |
     | Drivers  | 8                     |
     | Status   | Re-Dispatch Optimized |

    When I select project day with name '04-01-23'
    When I start performance tracing with dev tools
    When I right click on map at point with offset x: '-180' and y: '-193'
    When I click and the papaki to trigger refresh/update a request
    When I choose from the stop point right click choices to change state of points
    When I stop performance tracing with dev tools and i save the file to 'FirstTest'




      @pass
  Scenario:load a PP, go back to PP list and load to another one
    Given I navigate at lastmily login page 'https://dev2.lastmily.com/'
    When I fill login page username field with 'ups_thanos@lastmily.com'
    When I fill login page password field with '1234'
    When I click the login button
    When I choose from navbar project page button
    When I select project with name '1st project'
    Then Verify that the project day with name 'aeroporiko 14_12' has the following details
      | Title    | Value                   |
      | Dep Time | 11:30                   |
      | Distance | 1398.29km               |
      | Stops    | 767                     |
      | Drivers  | 11                      |
      | Status   | Un-Dispatched Optimized |
    Then Verify that the project day with name 'odiko + aeroporiko (6 lepta)' has the following details
      | Title    | Value                |
      | Dep Time | 09:30                |
      | Distance | 1510.01km            |
      | Stops    | 1327                 |
      | Drivers  | 17                   |
      | Status   | Dispatched Optimized |
    When I start performance tracing with dev tools
    When I select project day with name 'aeroporiko 14_12'
    When I click back button
    When I select project day with name 'odiko + aeroporiko (6 lepta)'
    When I click back button
    When I select project day with name 'aeroporiko 14_12'
    When I click back button
    When I select project day with name 'odiko + aeroporiko (6 lepta)'
    When I stop performance tracing with dev tools and i save the file to 'FirstTest'





  @pass  @unicodeHow?IdiditWIthanotherWay
  Scenario: hover on driver
    Given I navigate at lastmily login page 'https://dev2.lastmily.com/'
    When I fill login page username field with 'jim@lastmily.com'
    When I fill login page password field with 'asdf'
    When I click the login button
    When I choose from navbar project page button
    When I select project with name 'Dianomi'
    Then Verify that the project day with name '04-01-23' has the following details
     | Title    | Value                 |
     | Dep Time | 06:30                 |
     | Distance | 1723.01km             |
     | Stops    | 213                   |
     | Drivers  | 8                     |
     | Status   | Re-Dispatch Optimized |

    When I select project day with name '04-01-23'
    When I start performance tracing with dev tools
    When I hover on map with offset x: '45' and y: '200'
    Then Verify vehicle hover box is opened with last seen status 'Last seen: 10:11'
    When I click on map at point with offset x: '200' and y: '200'
    When I hover on map with offset x: '45' and y: '200'
    Then Verify vehicle hover box is opened with last seen status 'Last seen: 10:11'
    When I click on map at point with offset x: '200' and y: '200'
    When I hover on map with offset x: '45' and y: '200'
    Then Verify vehicle hover box is opened with last seen status 'Last seen: 10:11'
    When I click on map at point with offset x: '200' and y: '200'
    When I stop performance tracing with dev tools and i save the file to 'FirstTest'




  @pass
  Scenario: hover on sp
    Given I navigate at lastmily login page 'https://dev2.lastmily.com/'
    When I fill login page username field with 'jim@lastmily.com'
    When I fill login page password field with 'asdf'
    When I click the login button
    When I choose from navbar project page button
    When I select project with name 'Dianomi'
    Then Verify that the project day with name '04-01-23' has the following details
      | Title    | Value                 |
      | Dep Time | 06:30                 |
      | Distance | 1723.01km             |
      | Stops    | 213                   |
      | Drivers  | 8                     |
      | Status   | Re-Dispatch Optimized |

    When I select project day with name '04-01-23'
    When I start performance tracing with dev tools
    When I hover on map with offset x: '30' and y: '210'
    Then Verify stop point hover box is opened with name '0099522 - CHENGKAI ZHOU'
    When I click on map at point with offset x: '200' and y: '200'
    When I hover on map with offset x: '30' and y: '210'
    Then Verify stop point hover box is opened with name '0099522 - CHENGKAI ZHOU'
    When I click on map at point with offset x: '200' and y: '200'
    When I hover on map with offset x: '30' and y: '210'
    Then Verify stop point hover box is opened with name '0099522 - CHENGKAI ZHOU'
    When I click on map at point with offset x: '200' and y: '200'
    When I stop performance tracing with dev tools and i save the file to 'FirstTest'




#  @pass
#  Scenario: Time from right click on sp till window appears
#    Given I navigate at lastmily login page 'https://dev2.lastmily.com/'
#    When I fill login page username field with 'jim@lastmily.com'
#    When I fill login page password field with 'asdf'
#    When I click the login button
#    When I choose from navbar project page button
#    When I select project with name 'Dianomi'
#    Then Verify that the project day with name '04-01-23' has the following details
#     | Title    | Value                 |
#     | Dep Time | 06:30                 |
#     | Distance | 1723.01km             |
#     | Stops    | 213                   |
#     | Drivers  | 8                     |
#     | Status   | Re-Dispatch Optimized |
#
#    When I select project day with name '04-01-23'
#    When I start performance tracing with dev tools
#    When I right click on sp at point with offset x: '30' and y: '210' and wait keep time until windows opens

#
#  @pass
#  Scenario: Hover on Sp while Zooming
#    Given I navigate at lastmily login page 'https://dev2.lastmily.com/'
#    When I fill login page username field with 'jim@lastmily.com'
#    When I fill login page password field with 'asdf'
#    When I click the login button
#    When I choose from navbar project page button
#    When I select project with name 'Dianomi'
#    Then Verify that the project day with name '04-01-23' has the following details
#     | Title    | Value                 |
#     | Dep Time | 06:30                 |
#     | Distance | 1723.01km             |
#     | Stops    | 213                   |
#     | Drivers  | 8                     |
#     | Status   | Re-Dispatch Optimized |

#    When I select project day with name '04-01-23'
#    When I start performance tracing with dev tools
#    When I hover on map with offset x: '30' and y: '210'
#    Then Verify stop point hover box is opened with name '0099522 - CHENGKAI ZHOU'
#    When I scroll zoomin and zoom out at scales '3' for '2' times
#    Then Verify stop point hover box is opened with name '0099522 - CHENGKAI ZHOU'
#    When I stop performance tracing with dev tools and i save the file to 'hoverSpWhileZooming' where i edit log file for duration of js events




