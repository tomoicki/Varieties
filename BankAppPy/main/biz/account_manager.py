from main.model.user import User
from main.model.operations.payment_in import PaymentIn
from main.model.operations.withdraw import Withdraw
from main.model.account import Account
from main.db.dao import DAO
from main.biz.bank_history import BankHistory
from main.biz.authentication_manager import AuthenticationManager
from main.model.exceptions.exceptions import OperationIsNotAllowedException


class AccountManager:
    logged_user = None
    history = BankHistory()
    auth = AuthenticationManager()

    def payment_in(self, user: User, description: str, amount: float, account_id: int) -> bool:
        if amount <= 0:
            return False
        account = DAO.find_account_by_id(account_id)
        if account is None:
            return False
        success = account.income(amount)
        if not success:
            return False
        success = DAO.update_account_state(account)
        if not success:
            return False
        operation = PaymentIn(user, description, amount, account)
        success = self.auth.can_invoke_operation(operation, user)
        self.history.log_operation(operation, success)
        return success

    def payment_out(self, user: User, description: str, amount: float, account_id: int) -> bool:
        if amount <= 0:
            return False
        account = DAO.find_account_by_id(account_id)
        if account is None:
            return False
        operation = Withdraw(user, description, amount, account)
        success = self.auth.can_invoke_operation(operation, user)
        if not success:
            self.history.log_UnauthorizedOperation(operation, success)
            raise OperationIsNotAllowedException("Unauthorized operation")
        success = account.outcome(amount)
        if not success:
            self.history.log_operation(operation, success)
            return False
        success = DAO.update_account_state(account)
        if not success:
            self.history.log_operation(operation, success)
            return False
        return success

    def internal_payment(self, user: User, description: str, amount: float,
                         source_account_id: int, dest_account_id: int) -> bool:
        source_account = DAO.find_account_by_id(source_account_id)
        dest_account = DAO.find_account_by_id(dest_account_id)
        if source_account is None or dest_account is None:
            return False
        withdraw = Withdraw(user, description, amount, source_account)
        payment = PaymentIn(user, description, amount, dest_account)
        success = self.auth.can_invoke_operation(withdraw, user)
        if not success:
            self.history.log_UnauthorizedOperation(withdraw, success)
            raise OperationIsNotAllowedException("Unauthorized operation")
        success = source_account.outcome(amount)
        success = success and dest_account.income(amount)
        if success:
            success = DAO.update_account_state(source_account)
            if success:
                DAO.update_account_state(dest_account)
        self.history.log_operation(withdraw, success)
        self.history.log_operation(payment, success)
        return success

    # def alt_internal_payment(self, user: User, description: str, amount: float,
    #                          source_account: Account, dest_account: Account) -> bool:
    #     if amount < 0:
    #         return False
    #     withdraw = Withdraw(user, description, amount, source_account)
    #     payment = PaymentIn(user, description, amount, dest_account)
    #     success = self.auth.can_invoke_operation(withdraw, user)
    #     if not success:
    #         self.history.log_UnauthorizedOperation(withdraw, success)
    #         raise OperationIsNotAllowedException("Unauthorized operation")
    #     success = source_account.outcome(amount)
    #     success = success and dest_account.income(amount)
    #     if success:
    #         success = DAO.update_account_state(source_account)
    #         if success:
    #             DAO.update_account_state(dest_account)
    #     self.history.log_operation(withdraw, success)
    #     self.history.log_operation(payment, success)
    #     return success

    def log_in(self, user_name: str, password: str):
        self.logged_user = self.auth.log_in(user_name, password)
        return self.logged_user is not None

    def log_out(self, user: User):
        if self.auth.log_out(user):
            self.logged_user = None
            return True
        return False

    def get_logged_user(self):
        return self.logged_user
