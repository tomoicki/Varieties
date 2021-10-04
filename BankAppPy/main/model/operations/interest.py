from main.model.operations.operation_type import OperationType
from main.model.user import User
from main.model.account import Account
from main.model.operations.payment import Payment


class Interest(Payment):
    def __init__(self, user: User, description: str, amount: float, account: Account):
        super().__init__(user, description, OperationType.INTEREST, amount, account)

