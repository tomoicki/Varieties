Feature: AccountManager class unit tests

  Background: Set up background objects
      Given Create AccountManager instance

  Scenario Outline: Internal payments
      Given We have user with name <user_name>
      Given <user_name> has account number: <source_account_number> with amount: <source_amount>
      Given We have account number: <dest_account_number> with amount: <dest_amount>
      When User makes internal payment from acc:<source_account_number> to acc:<dest_account_number> with amount:<amount>
      Then Account <source_account_number> should have <source_expected_amount> and account <dest_account_number> should have <dest_expected_amount>
      Then Expected and calculated amounts should be equal for both

    Examples: Internal payments parameters
    |user_name   |source_account_number |source_amount  |dest_account_number |dest_amount  |amount |source_expected_amount |dest_expected_amount |
    |Eve         |1                     |200            |2                   |100          |158.5  |41.5                   |258.5                |
    |Tom         |11                    |999            |111                 |0            |998    |1                      |998                  |
    |Hobo        |5                     |0              |6                   |0            |100    |0                      |0                    |
    |Negative    |8                     |500            |9                   |0            |-100   |500                    |0                    |

  Scenario Outline: Payment in
      Given We have user with name <user_name>
      Given <user_name> has account number: <account_number> with amount: <starting_amount>
      When User makes payment in with amount:<amount>
      Then <user_name> account should have <expected_amount>
      Then Expected and calculated amounts should be equal

    Examples: Payment in parameters
    |user_name|account_number|starting_amount|amount|expected_amount|
    |Eve      |1             |100            |11    |111            |
    |Hobo     |0             |0              |0     |0              |
    |NegStart |999           |-100           |200   |100            |
    |NegAmo   |998           |123            |-50   |123            |
    |Float    |2             |111.11         |54.3  |165.41         |

  Scenario Outline: Payment out
      Given We have user with name <user_name>
      Given <user_name> has account number: <account_number> with amount: <starting_amount>
      When User makes payment out with amount:<amount>
      Then <user_name> account should have <expected_amount>
      Then Expected and calculated amounts should be equal

    Examples: Payment out parameters
    |user_name|account_number|starting_amount|amount|expected_amount|
    |Eve      |1             |100            |11    |89             |
    |Hobo     |0             |0              |10    |0              |
    |ZeroOut  |3             |50             |0     |50             |
    |NegStart |999           |-100           |200   |-100           |
    |NegAmo   |998           |123            |-50   |123            |
    |Float    |2             |111.11         |54.3  |56.81          |

