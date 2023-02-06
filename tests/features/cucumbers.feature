Feature: Cucumber Basket
  As a gardener,
  I want to carry cucumbers in a basket,
  So that I don't drop them all

  Scenario: Add cucumbers to a basket
    Given the basket has "2" cucumbers
    When "4" cucumbers are added to the basket
    Then the basket contains "6" cucumbers


  @smoke
  Scenario Outline:  Add cucumbers to basket with examples
    Given the basket has "<Initial>" cucumbers
    When "<Some>" cucumbers are added to the basket
    Then the basket contains "<Total>" cucumbers
    Examples: Amounts
      | Initial | Some | Total |
      | 1       | 5    | 6     |
      | 7       | 1    | 8     |
      | 5       | 1    | 6     |


  Scenario: Remove cucumbers from a basket
    Given the basket has "10" cucumbers
    When "4" cucumbers removed from the basket
    Then the basket contains "6" cucumbers

