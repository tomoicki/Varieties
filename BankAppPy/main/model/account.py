from dataclasses import dataclass
from .user import User


@dataclass
class Account:
    id: int
    amount: float
    owner: User

    def income(self, amount: float) -> bool:
        self.amount += amount
        return True

    def outcome(self, amount: float) -> bool:
        if self.amount < amount:
            return False
        self.amount -= amount
        return True

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int) -> None:
        self.id = id

    def get_amount(self) -> float:
        return self.amount

    def set_amount(self, amount: float) -> None:
        self.amount = amount

    def get_owner(self) -> User:
        return self.owner

    def set_owner(self, owner: User) -> None:
        self.owner = owner

