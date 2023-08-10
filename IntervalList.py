from typing import List

from IntervalListException import IntervalListException, IntervalListExceptionCode


def _input_validator(input_list: list):
    if len(input_list) != 2:
        raise IntervalListException(IntervalListExceptionCode.PARAMETER_NOT_FOUND)

    start = input_list[0]
    end = input_list[1]

    if end < start:
        raise IntervalListException(IntervalListExceptionCode.INVALID_PARAMETER)

    return input_list[0], input_list[1]


class IntervalList:
    def __init__(self):
        self._list = []

    def add(self, input_list: List[int]):
        start, end = _input_validator(input_list)

        for i in range(start, end):
            if i not in self._list:
                self._list.append(i)

        self._list = sorted(self._list)

        return

    def remove(self, input_list: List[int]):
        start, end = _input_validator(input_list)

        for i in range(start, end):
            if i in self._list:
                self._list.remove(i)

        return

    def print(self):
        if len(self._list) == 0:
            print("[)")
            return

        sub_list = [self._list[0]]
        for i in range(1, len(self._list)-1):
            if self._list[i-1] == (self._list[i] - 1) and self._list[i+1] == (self._list[i] + 1):
                continue
            else:
                sub_list.append(self._list[i])
        sub_list.append(self._list[-1])

        result = ""
        for idx, x in enumerate(sub_list):
            if idx % 2 == 0:
                result += f"[{x}, "
            else:
                result += f"{x+1}) "

        print(result)

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise IntervalListException(IntervalListExceptionCode.UNSUPPORTED_OPERATION)

        return max(self._list) < max(other._list)

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            raise IntervalListException(IntervalListExceptionCode.UNSUPPORTED_OPERATION)

        return max(self._list) <= max(other._list)

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise IntervalListException(IntervalListExceptionCode.UNSUPPORTED_OPERATION)

        return max(self._list) > max(other._list)

    def __ge__(self, other):
        if not isinstance(other, self.__class__):
            raise IntervalListException(IntervalListExceptionCode.UNSUPPORTED_OPERATION)

        return max(self._list) >= max(other._list)

    def __eq__(self, other):
        """
        _list 의 값이 모두 같으면 True, 아니면 False
        """
        if not isinstance(other, self.__class__):
            raise IntervalListException(IntervalListExceptionCode.UNSUPPORTED_OPERATION)

        if len(self._list) != len(other._list):
            return False

        for i in range(0, len(self._list)):
            if self._list[i] != other._list[i]:
                return False

        return True

    def __contains__(self, other):
        if not isinstance(other, self.__class__):
            raise IntervalListException(IntervalListExceptionCode.UNSUPPORTED_OPERATION)

        for i in other._list:
            if i not in self._list:
                return False

        return True
