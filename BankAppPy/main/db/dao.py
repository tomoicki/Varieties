from main.model.account import Account
from main.model.operation import Operation
from main.model.user import User


class DAO:
    @classmethod
    def find_user_by_name(cls, user_name: str):
        pass

    @classmethod
    def find_password_for_user(cls, user: User):
        pass

    @classmethod
    def find_account_by_id(cls, account_id: int):
        pass

    @classmethod
    def update_account_state(cls, account: Account):
        pass

    @classmethod
    def log_operation(cls, operation: Operation, success: bool):
        pass

