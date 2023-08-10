import unittest

from IntervalList import IntervalList
from IntervalListException import IntervalListException, IntervalListExceptionCode


class TestIntervalList(unittest.TestCase):
    def setUp(self) -> None:
        self.il = IntervalList()

    def tearDown(self) -> None:
        pass

    def test_parameter_not_found_case(self):
        # when
        with self.assertRaises(IntervalListException) as exc:
            self.il.add([1])

        # then
        self.assertEqual(IntervalListExceptionCode.PARAMETER_NOT_FOUND, exc.exception.exception_code)

    def test_parameter_invalid_parameter_case(self):
        # when
        with self.assertRaises(IntervalListException) as exc:
            self.il.add([10, 7])

        # then
        self.assertEqual(IntervalListExceptionCode.INVALID_PARAMETER, exc.exception.exception_code)

    def test_add(self):
        # given
        start = 1
        end = 5

        # when
        self.il.add([start, end])

        # then
        self.assertEqual([i for i in range(start, end)], self.il._list)

    def test_remove(self):
        # given
        start = 1
        end = 5
        self.il.add([start, end])
        new_end = 3

        # when
        self.il.remove([new_end, end])

        # then
        self.assertEqual([i for i in range(start, new_end)], self.il._list)

    def test_operator_type_check(self):
        # given
        start, end = 1, 5
        self.il.add([start, end])

        # when
        with self.assertRaises(IntervalListException) as exc:
            result = self.il < 9

        # then
        self.assertTrue(IntervalListExceptionCode.UNSUPPORTED_OPERATION, exc.exception.exception_code)

    def test_little(self):
        # given
        start = 1
        end_1 = 5
        end_2 = 7
        self.il.add([start, end_1])
        il_2 = IntervalList()
        il_2.add([start, end_2])

        # when
        result = self.il < il_2

        # then
        self.assertTrue(result)

    def test_little_or_equal_little_case(self):
        # given
        start = 1
        end_1 = 5
        end_2 = 7
        self.il.add([start, end_1])
        il_2 = IntervalList()
        il_2.add([start, end_2])

        # when
        result = self.il <= il_2

        # then
        self.assertTrue(result)

    def test_little_or_equal_equal_case(self):
        # given
        start = 1
        end = 5
        self.il.add([start, end])
        il_2 = IntervalList()
        il_2.add([start, end])

        # when
        result = self.il <= il_2

        # then
        self.assertTrue(result)

    def test_greater(self):
        # given
        start = 1
        end_1 = 9
        end_2 = 7
        self.il.add([start, end_1])
        il_2 = IntervalList()
        il_2.add([start, end_2])

        # when
        result = self.il > il_2

        # then
        self.assertTrue(result)

    def test_greater_or_equal_greater_case(self):
        # given
        start = 1
        end_1 = 9
        end_2 = 7
        self.il.add([start, end_1])
        il_2 = IntervalList()
        il_2.add([start, end_2])

        # when
        result = self.il >= il_2

        # then
        self.assertTrue(result)

    def test_greater_or_equal_equal_case(self):
        # given
        start = 1
        end = 5
        self.il.add([start, end])
        il_2 = IntervalList()
        il_2.add([start, end])

        # when
        result = self.il >= il_2

        # then
        self.assertTrue(result)

    def test_equal_not_equal_length_case(self):
        # given
        start = 5
        end_1, end_2 = 7, 10
        self.il.add([start, end_1])
        il_2 = IntervalList()
        il_2.add([start, end_2])

        # when
        result = self.il == il_2

        # then
        self.assertFalse(result)

    def test_equal_equal_length_not_equal_value_case(self):
        # given
        start_1, start_2 = 1, 2
        end_1, end_2 = 4, 5
        self.il.add([start_1, end_1])
        il_2 = IntervalList()
        il_2.add([start_2, end_2])

        # when
        result = self.il == il_2

        # then
        self.assertFalse(result)

    def test_equal_equal_case(self):
        # given
        start, end = 1, 5
        self.il.add([start, end])
        il_2 = IntervalList()
        il_2.add([start, end])

        # when
        result = self.il == il_2

        # then
        self.assertTrue(result)

    def test_contains_false_case(self):
        # given
        start, end = 1, 5
        start_2, end_2 = 3, 7
        self.il.add([start, end])
        il_2 = IntervalList()
        il_2.add([start_2, end_2])

        # when
        result = self.il in il_2

        # then
        self.assertFalse(result)

    def test_contains_true_case(self):
        # given
        start, end = 3, 6
        start_2, end_2 = 1, 10
        self.il.add([start, end])
        il_2 = IntervalList()
        il_2.add([start_2, end_2])

        # when
        result = self.il in il_2

        # then
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
