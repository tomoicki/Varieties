from dataclasses import dataclass
from abc import ABC
from main.model.operation import Operation
from main.model.account import Account


@dataclass
class Payment(Operation, ABC):
    amount: float
    account: Account

    def get_amount(self) -> float:
        return self.amount

    def get_account(self) -> Account:
        return self.account


