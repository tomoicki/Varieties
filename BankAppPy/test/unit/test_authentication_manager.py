import unittest
from unittest.mock import MagicMock
from main.biz.account_manager import AccountManager
from main.db.dao import DAO
from main.model.password import Password
from main.model.user import User
from main.model.role import Role
from main.model.operation import Operation
from main.model.operations.operation_type import OperationType
from main.biz.authentication_manager import AuthenticationManager
from main.model.exceptions.exceptions import UserUnknownOrBadPasswordException


class TestAuthenticationManager(unittest.TestCase):
    def setUp(self) -> None:
        self.auth = AuthenticationManager()
        self.account_manager = AccountManager()
        self.password = Password(101, 'my_password')
        self.role_user = Role(0, 'user')
        self.user1 = User(101, "Eve", self.role_user)
        self.user2 = User(102, "Adam", self.role_user)
        self.operation_pay_in = Operation(self.user1, "pay in", OperationType.PAYMENT_IN)

    # ===============================================================================
    #  check_password
    def test_check_password_false(self) -> None:
        # given that provided password is different than user-password
        # when we try to check password
        success = self.auth.check_password(self.password, 'some_password')
        # then function should return False
        self.assertFalse(success)

    def test_check_password_true(self) -> None:
        # given that provided password is same as user-password
        # when we try to check password
        success = self.auth.check_password(self.password, 'my_password')
        # then function should return True
        self.assertTrue(success)

    # ===============================================================================
    #  log_in
    def test_log_in_bad_user(self) -> None:
        # given that provided username doesn't correspond with any User in database
        DAO.find_user_by_name = MagicMock(return_value=None)
        # when we invoke self.auth.log_in
        with self.assertRaises(UserUnknownOrBadPasswordException):
            success = self.auth.log_in("user_name", 'user_pass')
            # error should be raised and function should return False
            self.assertFalse(success)

    def test_log_in_bad_password(self) -> None:
        # given that provided user is found
        DAO.find_user_by_name = MagicMock(return_value=self.user1)
        # but passwords dont match
        self.auth.check_password = MagicMock(return_value=False)
        # when we invoke self.auth.log_in
        with self.assertRaises(UserUnknownOrBadPasswordException):
            success = self.auth.log_in("user_name", 'user_pass')
            # error should be raised and function should return False
            self.assertFalse(success)

    def test_log_in_success(self) -> None:
        # given that provided user is found
        DAO.find_user_by_name = MagicMock(return_value=self.user1)
        # and passwords match
        self.auth.check_password = MagicMock(return_value=True)
        # when we invoke self.auth.log_in
        user = self.auth.log_in("Eve", 'my_password')
        # then function should success and return user
        self.assertEqual(user, self.user1)

    # ===============================================================================
    #  log_out
    def test_log_out(self) -> None:
        success = self.auth.log_out(self.user1)
        self.assertTrue(success)

    # ===============================================================================
    #  can_invoke_operation
    def test_can_invoke_operation_if_admin(self) -> None:
        # given that the user provided has role "Admin"
        role_admin = Role(1000, 'Admin')
        admin = User(111, 'God', role_admin)
        # when we run self.auth.can_invoke_operation
        success = self.auth.can_invoke_operation(self.operation_pay_in, admin)
        # then function should return True
        self.assertTrue(success)

    def test_can_invoke_operation_if_payment_in(self) -> None:
        # given that the operation is PAYMENT_IN
        # when we run self.auth.can_invoke_operation
        success = self.auth.can_invoke_operation(self.operation_pay_in, self.user1)
        # then function should return True
        self.assertTrue(success)

    def test_can_invoke_operation_if_withdraw_succes(self) -> None:
        # given that the operation is WITHDRAW
        withdraw = Operation(self.user1, 'withdraw', OperationType.WITHDRAW)
        # and user.id is the same as operation.user.id
        # when we run self.auth.can_invoke_operation
        success = self.auth.can_invoke_operation(withdraw, self.user1)
        # then function should return True
        self.assertTrue(success)

    def test_can_invoke_operation_if_withdraw_fail(self) -> None:
        # given that the operation is WITHDRAW
        withdraw = Operation(self.user2, 'withdraw', OperationType.WITHDRAW)
        # and user.id is different than operation.user.id
        # when we run self.auth.can_invoke_operation
        success = self.auth.can_invoke_operation(withdraw, self.user1)
        # then function should return True
        self.assertFalse(success)





