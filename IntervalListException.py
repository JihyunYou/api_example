from enum import Enum


class IntervalListExceptionCode(Enum):
    INVALID_PARAMETER = "invalid parameter"
    PARAMETER_NOT_FOUND = "parameter not found"
    UNSUPPORTED_OPERATION = "unsupported operation"


class IntervalListException(Exception):
    def __init__(self, exception_code):
        super().__init__(exception_code)

        self.exception_code = exception_code
