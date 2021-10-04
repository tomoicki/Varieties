from main.db.dao import DAO
from main.model.user import User
from main.model.operations.login import LogIn
from main.model.operations.logout import LogOut
from main.model.operation import Operation
from main.model.account import Account


class BankHistory:
    def log_operation(self, operation: Operation, success: bool) -> None:
        DAO.log_operation(operation, success)

    def login_success(self, user: User) -> None:
        o = LogIn(user, "Logowanie")
        self.log_operation(o, True)

    def login_failure(self, user, info: str) -> None:
        o = LogIn(None, info)
        self.log_operation(o, False)

    def logout(self, user: User) -> None:
        o = LogOut(user, "Log out")
        self.log_operation(o, True)

    def log_PaymentIn(self, account: Account, amount: float, success: bool):
        pass

    def log_PaymentOut(self, account: Account, amount: float, success: bool):
        pass

    def log_UnauthorizedOperation(self, operation: Operation, success: bool):
        pass
