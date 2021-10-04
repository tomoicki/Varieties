import unittest
import pytest
from unittest.mock import MagicMock, patch
from main.biz.account_manager import AccountManager
from main.db.dao import DAO
from main.model.account import Account
from main.model.user import User
from main.model.role import Role
from main.biz.interest_operator import InterestOperator


class TestInterestOperator(unittest.TestCase):
    def setUp(self) -> None:
        self.interest_operator = InterestOperator(AccountManager())
        self.user = User(1, "Eve", Role(999, "regular_user"))
        self.eve_account = Account(101, 1000, self.user)

    @patch('main.biz.bank_history.BankHistory.log_operation')
    def test_count_interest_for_account(self, log_operation_mock) -> None:
        # eve_account amount before interest
        amount_before = self.eve_account.get_amount()
        # eve_account amount before interest but after calculations
        amount_before_but_after = amount_before + amount_before * self.interest_operator.interest_factor
        # amount_before_but_after = 1200
        # invoke count_interest_for_account()
        DAO.find_user_by_name = MagicMock(return_value=self.user)
        DAO.find_account_by_id = MagicMock(return_value=self.eve_account)
        self.interest_operator.count_interest_for_account(self.eve_account)
        # eve_account amount after interest
        amount_after = self.eve_account.get_amount()
        self.assertEqual(amount_before_but_after, amount_after)
        log_operation_mock.assert_called_once()


@pytest.mark.parametrize("starting_amount,expected_amount",
                         [(-100, -100), (0, 0), (100, 120), (55.3, 66.36)])
def test_count_interest_for_account_parametrized(starting_amount, expected_amount) -> None:
    # setUp
    interest_operator = InterestOperator(AccountManager())
    eve = User(1, "Eve", Role(999, "regular_user"))
    eve_account = Account(101, starting_amount, eve)
    # eve_account amount before interest
    amount_before = eve_account.get_amount()
    # eve_account amount before interest but after calculations
    amount_before_but_after = amount_before + amount_before * interest_operator.interest_factor
    # invoke count_interest_for_account()
    DAO.find_user_by_name = MagicMock(return_value=eve)
    DAO.find_account_by_id = MagicMock(return_value=eve_account)
    interest_operator.count_interest_for_account(eve_account)
    # eve_account amount after interest
    amount_after = eve_account.get_amount()
    assert expected_amount == amount_after

