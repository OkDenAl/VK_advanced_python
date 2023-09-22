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
            f_reader = FileFilterReader("file.txt", [])

            self.assertEqual([], f_reader.find_line())
            expected_calls = [
                mock.call("file.txt"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_few_searching_words(self):
        with mock.patch("file_reader.open") as mock_fetch:
            mock_fetch.return_value = self.mock_file_data
            f_reader = FileFilterReader("file.txt", ["роза", "ЛЮБЛЮ"])

            self.assertEqual(["а Роза упала на Лапу Азора", "люблю розы"],
                             f_reader.find_line())
            expected_calls = [
                mock.call("file.txt"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_lines_found(self):
        with mock.patch("file_reader.open") as mock_fetch:
            mock_fetch.return_value = self.mock_file_data
            f_reader = FileFilterReader("file.txt", ["роза"])

            self.assertEqual(["а Роза упала на Лапу Азора"],
                             f_reader.find_line())
            expected_calls = [
                mock.call("file.txt"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_lines_not_found(self):
        with mock.patch("file_reader.open") as mock_fetch:
            mock_fetch.return_value = self.mock_file_data
            f_reader = FileFilterReader("file.txt", ["розы"])

            self.assertEqual([], f_reader.find_line())
            expected_calls = [
                mock.call("file.txt"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_cant_open_the_file(self):
        with self.assertRaises(FileNotFoundError) as err:
            FileFilterReader("unknown.txt", ["розы"])

        self.assertEqual("[Errno 2] No such file or directory: 'unknown.txt'",
                         str(err.exception))
        self.assertEqual(FileNotFoundError, type(err.exception))
