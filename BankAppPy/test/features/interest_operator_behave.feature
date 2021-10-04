Feature: InterestOperator class unit tests

  Background: Set up background objects
      Given Create InterestOperator instance

  Scenario Outline: Count interest
      Given We have user with the name <user_name>
      Given He/She has account with amount: <starting_amount>
      When The interest is calculated
      Then His/Her account should have: <expected_amount>
      Then Calculated amount should equal expected amount

    Examples: Payment out parameters
    |user_name|starting_amount|expected_amount|
    |Eve      |100            |120            |
    |Hobo     |0              |0              |
    |Negative |-100           |-100           |
    |Float    |55.3           |66.36          |

