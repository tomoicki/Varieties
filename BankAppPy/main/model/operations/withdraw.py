from .payment import Payment
from .operation_type import OperationType
from main.model.user import User
from main.model.account import Account


class Withdraw(Payment):
    def __init__(self, user: User, description: str, amount: float, account: Account):
        super().__init__(user, description, OperationType.WITHDRAW, amount, account)

