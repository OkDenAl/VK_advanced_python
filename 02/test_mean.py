import unittest
from io import StringIO
from unittest import mock
from mean import mean
from mean import InvalidParamError
import sys


class TestMean(unittest.TestCase):
    def test_mean_2_with_print(self):
        with mock.patch('time.time') as mock_fetch:
            mock_fetch.side_effect = [0,1,0,2]
            captured_output = StringIO()
            sys.stdout = captured_output

            @mean(3)
            def func(x):
                return x

            x=func(1)
            self.assertEqual(captured_output.getvalue(), "Среднее время выполнения последних"
                                                         " 1 вызовов функции func: 1.0 [1, 0, 0]\n")
            self.assertEqual(x,1)
            captured_output.truncate(0)
            captured_output.seek(0)
            x=func(2)
            self.assertEqual(captured_output.getvalue(), "Среднее время выполнения последних"
                                                         " 2 вызовов функции func: 1.5 [1, 2, 0]\n")
            self.assertEqual(x, 2)
            self.assertEqual(mock_fetch.call_count, 4)

    def test_mean_1_print(self):
        with mock.patch('builtins.print') as mock_fetch:
            @mean(3)
            def func(x):
                return x

            x=func(1)
            self.assertEqual(x, 1)
            self.assertEqual(mock_fetch.call_count, 1)

    def test_mean_many_print(self):
        with mock.patch('builtins.print') as mock_fetch:
            @mean(3)
            def func(x):
                return x

            for i in range(100):
                func(1)
            self.assertEqual(mock_fetch.call_count, 100)

    def test_mean_invalid_param(self):
        with self.assertRaises(InvalidParamError) as err:
            @mean(-1)
            def func(x):
                return x
        self.assertEqual("invalid k param value", str(err.exception))
        self.assertEqual(InvalidParamError, type(err.exception))
