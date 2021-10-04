
class OperationIsNotAllowedException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class UserUnknownOrBadPasswordException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

