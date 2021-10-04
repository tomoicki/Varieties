from main.model.user import User
from main.db.dao import DAO
from main.model.exceptions.exceptions import UserUnknownOrBadPasswordException
from main.biz.bank_history import BankHistory
from main.model.password import Password
from main.model.operation import Operation
from main.model.operations.operation_type import OperationType


class AuthenticationManager:
    history = BankHistory()

    def hash_password(self, password) -> str:
        return password

    def check_password(self, passwd: Password, password: str):
        hashed_password = self.hash_password(password)
        return passwd.get_passwd() == hashed_password

    def log_in(self, user_name: str, password):
        user = DAO.find_user_by_name(user_name)
        if user is None:
            self.history.login_failure(None, f"Zła nazwa użytkownika: {user_name}")
            raise UserUnknownOrBadPasswordException("Bad password")
        passwd = DAO.find_password_for_user(user)
        if self.check_password(passwd, password):
            self.history.login_success(user)
            return user
        else:
            self.history.login_failure(user, "Bad Password")
            raise UserUnknownOrBadPasswordException("Bad password")

    def log_out(self, user: User):
        self.history.logout(user)
        return True

    def can_invoke_operation(self, operation: Operation, user: User):
        if user.get_role().get_name() == 'Admin':
            return True
        if operation.get_type() == OperationType.PAYMENT_IN:
            return True
        if operation.get_type() == OperationType.WITHDRAW:
            return user.get_id() == operation.get_user().get_id()
        return False


