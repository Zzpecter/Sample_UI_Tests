Feature:
  Use the website to run tests
  So that I can find practice my testing skills
  As a AT bootcamp trainee
  I want to be able to test GUI elements

  Scenario: Clicking on a button
    Given I want food in "AR51 1AA"
    When I search for restaurants
    Then I should see some restaurants in "AR51 1AA"

  Scenario: Search for restaurants in a different area
    Given I want food in "SE1 5RW"
    When I search for restaurants
    Then I should see some restaurants in "SE1 5RW"

  Scenario: Search for restaurants in an invalid area
    Given I want food in an invalid location
    When I search for restaurants
    Then I should see an error message