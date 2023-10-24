from unittest import TestCase
from unittest import mock
import requests

from utils import get_common_words


class TestMostCommonWords(TestCase):
    def setUp(self):
        self.content = b'<html><head><title>Href Attribute Example</title>' \
                       b'</head><body><h1>Href Attribute Example</h1><p><a>' \
                       b'The freeCodeCamp Contribution Page</a> shows you how Attribute ' \
                       b'and where you can contribute to freeCodeCamp\'s' \
                       b' community and growth.</p></body></html>'

    def test_most_common_1(self):
        with mock.patch("requests.get") as mock_fetch:
            response = requests.Response()
            response._content = self.content

            mock_fetch.return_value = response
            common_words = get_common_words(1, "url")

            self.assertEqual({'Attribute': 3}, common_words)
            expected_calls = [
                mock.call("url"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_most_common_more_then_1(self):
        with mock.patch("requests.get") as mock_fetch:
            response = requests.Response()
            response._content = self.content

            mock_fetch.return_value = response
            common_words = get_common_words(3, "url")

            self.assertEqual({'Attribute': 3, 'you': 2, 'and': 2}, common_words)
            expected_calls = [
                mock.call("url"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)
