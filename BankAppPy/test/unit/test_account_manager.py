import unittest
from unittest.mock import MagicMock
from main.biz.account_manager import AccountManager
from main.db.dao import DAO
from main.model.account import Account
from main.model.user import User
from main.model.role import Role
from main.biz.authentication_manager import AuthenticationManager
from main.model.exceptions.exceptions import OperationIsNotAllowedException


class TestAccountManager(unittest.TestCase):
    def setUp(self) -> None:
        self.account_manager = AccountManager()
        self.role_user = Role(0, 'user')
        self.user1 = User(101, "Eve", self.role_user)
        self.user2 = User(102, "Grace", self.role_user)
        self.account1 = Account(1, 100, self.user1)
        self.account11 = Account(11, 50, self.user1)
        self.account2 = Account(2, 0, self.user2)

    # ===============================================================================
    #  payment_in
    def test_payment_in_account_invalid(self) -> None:
        # given that the account doesn't exist
        DAO.find_account_by_id = MagicMock(return_value=None)
        # when we try to make payment_in
        success = self.account_manager.payment_in(self.user1, 'desc', 1.1, account_id=1)
        # then payment_in should return false
        self.assertFalse(success)

    def test_payment_in_income_failure(self) -> None:
        # given that account exists and is found
        DAO.find_account_by_id = MagicMock(return_value=self.account1)
        # but the income function doesn't work
        self.account1.income = MagicMock(return_value=False)
        # when we try to make payment_in
        success = self.account_manager.payment_in(self.user1, 'desc', 1.1, account_id=1)
        # then payment_in should return false
        self.assertFalse(success)

    def test_payment_in_update_account_state_failure(self) -> None:
        # given that account exists and is found
        DAO.find_account_by_id = MagicMock(return_value=self.account1)
        # and the income function works
        self.account1.income = MagicMock(return_value=True)
        # but update_account_state() fails
        DAO.update_account_state = MagicMock(return_value=False)
        # when we try to make payment_in
        success = self.account_manager.payment_in(self.user1, 'desc', 1.1, account_id=1)
        # then payment_in should return false
        self.assertFalse(success)

    def test_payment_in_negative_amount(self) -> None:
        # given that we provide negative amount as payment_in
        amount = -1
        # when we try to make payment_in
        success = self.account_manager.payment_in(self.user1, 'desc', amount, account_id=1)
        # then payment_in should return false
        self.assertFalse(success)

    def test_payment_in_success(self) -> None:
        # given that account exists and is found
        DAO.find_account_by_id = MagicMock(return_value=self.account1)
        # and the income function works
        Account.income = MagicMock(return_value=True)
        # and update_account_state() works
        DAO.update_account_state = MagicMock(return_value=True)
        AuthenticationManager.can_invoke_operation = MagicMock(return_value=True)
        # when we try to make payment_in
        success = self.account_manager.payment_in(self.user1, 'desc', 1.1, account_id=1)
        # then payment_in should return true
        self.assertTrue(success)

    # ===============================================================================
    # payment_out
    def test_payment_out_account_invalid(self) -> None:
        # given that the account doesn't exist
        DAO.find_account_by_id = MagicMock(return_value=None)
        # when we try to make payment_out
        success = self.account_manager.payment_out(self.user1, 'desc', 1.1, account_id=1)
        # then payment_in should return false
        self.assertFalse(success)

    def test_payment_out_unauthorized_user(self) -> None:
        # given that account exists and is found
        DAO.find_account_by_id = MagicMock(return_value=self.account1)
        # but user is unauthorized
        AuthenticationManager.can_invoke_operation = MagicMock(return_value=False)
        # when we try to make payment_out
        with self.assertRaises(OperationIsNotAllowedException):
            success = self.account_manager.payment_out(self.user1, 'desc', 1.1, account_id=2)
            # then payment_out should raise OperationIsNotAllowedException
            self.assertFalse(success)

    def test_payment_out_outcome_failure(self) -> None:
        # given that account exists and is found
        DAO.find_account_by_id = MagicMock(return_value=self.account1)
        # but the outcome function returns false
        self.account1.outcome = MagicMock(return_value=False)
        # when we try to make payment_in
        success = self.account_manager.payment_out(self.user1, 'desc', 999999, account_id=1)
        # then payment_in should return false
        self.assertFalse(success)

    def test_payment_out_update_account_state_failure(self) -> None:
        # given that account exists and is found
        DAO.find_account_by_id = MagicMock(return_value=self.account1)
        # and the outcome function returns True
        AuthenticationManager.can_invoke_operation = MagicMock(return_value=True)
        self.account1.outcome = MagicMock(return_value=True)
        # but update_account_state() fails
        DAO.update_account_state = MagicMock(return_value=False)
        # when we try to make payment_in
        success = self.account_manager.payment_out(self.user1, 'desc', 1.1, account_id=1)
        # then payment_out should return false
        self.assertFalse(success)

    def test_payment_out_success(self) -> None:
        # given that account exists and is found
        DAO.find_account_by_id = MagicMock(return_value=self.account1)
        # and the outcome function works
        self.account1.income = MagicMock(return_value=True)
        # and update_account_state() works
        DAO.update_account_state = MagicMock(return_value=True)
        # when we try to make payment_out
        success = self.account_manager.payment_out(self.user1, 'desc', 1.1, account_id=1)
        # then payment_in should return true
        self.assertTrue(success)

    # ===============================================================================
    #  internal_payment
    def test_internal_payment_account_invalid(self) -> None:
        # given that either one of the accounts doesnt exist
        DAO.find_account_by_id = MagicMock(return_value=None)
        # when we try to make internal_payment
        success = self.account_manager.internal_payment(self.user1, 'desc', 10, 1, 11)
        # then payment_in should return false
        self.assertFalse(success)

    def test_internal_payment_unauthorized_user(self) -> None:
        # given that both accounts exist and are found
        DAO.find_account_by_id = MagicMock(return_value=self.account1)
        DAO.find_account_by_id = MagicMock(return_value=self.account2)
        # but user is unauthorized
        AuthenticationManager.can_invoke_operation = MagicMock(return_value=False)
        # when we try to make internal_payment
        with self.assertRaises(OperationIsNotAllowedException):
            success = self.account_manager.internal_payment(self.user1, 'desc', 1.1, 1, 11)
            # then payment_out should raise OperationIsNotAllowedException
            self.assertFalse(success)

    def test_internal_payment_income_or_outcome_fails(self) -> None:
        # given that both accounts exist and are found
        DAO.find_account_by_id = MagicMock(return_value=self.account1)
        DAO.find_account_by_id = MagicMock(return_value=self.account2)
        # and user is authorized
        AuthenticationManager.can_invoke_operation = MagicMock(return_value=True)
        # but income/outcome fails
        # when we try to make internal_payment
        success = self.account_manager.internal_payment(self.user1, 'desc', 10, 1, 11)
        # then payment_in should return False
        self.assertFalse(success)

    def test_internal_payment_success(self) -> None:
        # given that both accounts exist and are found
        DAO.find_account_by_id = MagicMock(return_value=self.account1)
        DAO.find_account_by_id = MagicMock(return_value=self.account2)
        # and user is authorized
        AuthenticationManager.can_invoke_operation = MagicMock(return_value=True)
        # and income/outcome succeeds
        Account.income = MagicMock(return_value=True)
        Account.outcome = MagicMock(return_value=True)
        DAO.update_account_state = MagicMock(return_value=True)
        # when we try to make internal_payment
        success = self.account_manager.internal_payment(self.user1, 'desc', 10, 1, 111)
        # then payment_in should return True
        self.assertTrue(success)

    # ===============================================================================
    #  log_in
    def test_log_in_fail(self) -> None:
        # given that we provide bad username/password
        AuthenticationManager.log_in = MagicMock(return_value=None)
        # when we try to log_in
        success = self.account_manager.log_in('username', 'pass')
        # then log_in should return False
        self.assertFalse(success)

    def test_log_in_success(self) -> None:
        # given that we provide good username/password
        AuthenticationManager.log_in = MagicMock(return_value=self.user1)
        # when we try to log_in
        success = self.account_manager.log_in('username', 'pass')
        # then log_in should return True
        self.assertTrue(success)

    # ===============================================================================
    #  log_out
    def test_log_out_fail(self) -> None:
        # given that something fails during auth.log_out
        AuthenticationManager.log_out = MagicMock(return_value=False)
        # when we try to log_out
        success = self.account_manager.log_out(self.user1)
        # then log_in should return False
        self.assertFalse(success)

    def test_log_out_success(self) -> None:
        # given that auth.log_out works
        AuthenticationManager.log_out = MagicMock(return_value=True)
        # when we try to log_out# when we try to log_in
        success = self.account_manager.log_out(self.user1)
        # then log_in should return True
        self.assertTrue(success)
