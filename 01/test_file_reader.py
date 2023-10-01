import io
import unittest
from unittest import mock
from file_reader import FileFilterReader


class TestFileFilterReader(unittest.TestCase):
    def setUp(self):
        self.mock_file_data = io.StringIO("а Роза упала на Лапу Азора\n"
                                          "люблю розы\n"
                                          "просто строка по приколу")

    def test_no_searching_words(self):
        with mock.patch("file_reader.open") as mock_fetch:
            mock_fetch.return_value = self.mock_file_data
            with self.assertRaises(StopIteration) as err:
                next(FileFilterReader("test.txt", []).find_line())

            self.assertEqual(StopIteration, type(err.exception))

    def test_few_searching_words(self):
        with mock.patch("file_reader.open") as mock_fetch:
            mock_fetch.return_value = self.mock_file_data
            f_reader = FileFilterReader("file.txt", ["роза", "ЛЮБЛЮ"]).find_line()

            res_list = []
            for _ in range(3):
                res = next(f_reader)
                if res is not None:
                    res_list.append(res)
            self.assertEqual(["а Роза упала на Лапу Азора", "люблю розы"], res_list)
            expected_calls = [
                mock.call("file.txt"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_lines_found(self):
        with mock.patch("file_reader.open") as mock_fetch:
            mock_fetch.return_value = self.mock_file_data
            f_reader = FileFilterReader("file.txt", ["роза"]).find_line()

            res_list = []
            for _ in range(3):
                res = next(f_reader)
                if res is not None:
                    res_list.append(res)

            self.assertEqual(["а Роза упала на Лапу Азора"], res_list)
            expected_calls = [
                mock.call("file.txt"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_lines_not_found(self):
        with mock.patch("file_reader.open") as mock_fetch:
            mock_fetch.return_value = self.mock_file_data
            f_reader = FileFilterReader("file.txt", ["розы"]).find_line()
            res_list = []
            for _ in range(3):
                res = next(f_reader)
                if res is not None:
                    res_list.append(res)
            self.assertEqual([], [])
            expected_calls = [
                mock.call("file.txt"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)
            with self.assertRaises(StopIteration) as err:
                next(f_reader)

            self.assertEqual(StopIteration, type(err.exception))

    def test_cant_open_the_file(self):
        with self.assertRaises(FileNotFoundError) as err:
            FileFilterReader("unknown.txt", ["розы"])

        self.assertEqual("[Errno 2] No such file or directory: 'unknown.txt'",
                         str(err.exception))
        self.assertEqual(FileNotFoundError, type(err.exception))
