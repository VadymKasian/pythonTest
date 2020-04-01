Feature: showing off behave

  Scenario: run a simple test
    Given open browser
    Then type search query
    Then press book filter
    Then add tooks to list
    Then check book from url contains in list