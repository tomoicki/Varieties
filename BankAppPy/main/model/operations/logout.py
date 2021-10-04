from main.model.operations.log_operation import LogOperation
from main.model.operations.operation_type import OperationType


class LogOut(LogOperation):
    def __init__(self, user, description: str):
        super().__init__(user, description, OperationType.LOG_OUT)

