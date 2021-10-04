from dataclasses import dataclass
from main.model.operations.operation_type import OperationType
from .user import User


@dataclass
class Operation:
    user: User
    description: str
    type: OperationType

    def get_user(self) -> User:
        return self.user

    def get_description(self) -> str:
        return self.description

    def get_type(self) -> OperationType:
        return self.type






