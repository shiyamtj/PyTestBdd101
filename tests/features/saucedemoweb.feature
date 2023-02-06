@web @smoke
Feature: SauceDemo page features
  As a web surfer,
  I want to search products,
  So I  can order and buy items.

  Background:
    Given the SauceDemo login page is displayed

  Scenario: Basic login
    When the user login with username as "standard_user" and password as "secret_sauce"
    Then the user should able to see dashboard loaded
