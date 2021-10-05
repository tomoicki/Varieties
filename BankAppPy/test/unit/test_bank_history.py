import unittest
from unittest.mock import patch
from main.model.user import User
from main.model.role import Role
from main.model.operation import Operation
from main.model.operations.operation_type import OperationType
from main.biz.bank_history import BankHistory


class TestBankHistory(unittest.TestCase):
    def setUp(self) -> None:
        self.history = BankHistory()
        self.user1 = User(1, "Eve", Role(999, 'normal_user'))
        self.operation = Operation(self.user1, "desc", OperationType.PAYMENT_IN)

    @patch('main.db.dao.DAO.log_operation')
    def test_log_operation(self, dao_log_operation_mock) -> None:
        self.history.log_operation(self.operation, True)
        dao_log_operation_mock.assert_called_once()

    @patch('main.biz.bank_history.BankHistory.log_operation')
    def test_login_success(self, log_operation_mock) -> None:
        self.history.login_success(self.user1)
        log_operation_mock.assert_called_once()

    @patch('main.biz.bank_history.BankHistory.log_operation')
    def test_login_failure(self, log_operation_mock) -> None:
        self.history.login_failure(self.user1, "info")
        log_operation_mock.assert_called_once()

    @patch('main.biz.bank_history.BankHistory.log_operation')
    def test_logout(self, log_operation_mock) -> None:
        self.history.logout(self.user1)
        log_operation_mock.assert_called_once()
