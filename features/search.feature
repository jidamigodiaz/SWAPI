Feature: Search endpoint


  @high @regression @smoke
  Scenario: Root resources should provide information for all resources
    Given I get from "https://swapi.dev/api/" with suffix "?search"
    Then I should see a response code "200"
    And I should see "films, people, planets, species, starships, vehicles" list in the body response
    And I should see a list of fields named "films, people, planets, species, starships, vehicles" starting with "https://" in body response


  @high @regression @smoke
  Scenario Outline: Search endpoint works as expected
    Given I get from "https://swapi.dev/api/" with suffix "<parameter>"
    Then I should see a response code "200"
    And I should see an "url" in each "results" of response
    And I should see a "url" string field in each "results" of response starting with "https://"
    And I should see an "name" in each "results" of response
    And I should see an "created" in each "results" of response
    And I should see an "edited" in each "results" of response
    Examples:
      | parameter         |
      | people/?search    |
      | planets/?search   |
      | starships/?search |
      | vehicles/?search  |


  @high @regression @smoke
  Scenario Outline: Check url included in body response
    Given I get from "https://swapi.dev/api/" with suffix "people/?search"
    Then I should see one "results" with name "<name>"
    When I get details from element with name "<name>" in "results" of response
    Then I should see a response code "200"
    And I should see "name, height, mass, birth_year, gender, url" list in the body response
    And I should see a list of fields named "url" starting with "https://" in body response
    Examples:
      | name            |
      | Luke Skywalker  |
      | C-3PO           |

