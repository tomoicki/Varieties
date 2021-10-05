from main.model.operation import Operation
from main.model.operations.operation_type import OperationType


class LogOperation(Operation):
    def __init__(self, user, description: str, type: OperationType):
        super().__init__(user, description, type)


