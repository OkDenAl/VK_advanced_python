import unittest
from unittest import mock
from jsonparser import parse_json
from jsonparser import InvalidRequiredFieldError


class TestJsonParser(unittest.TestCase):
    def setUp(self):
        self.dummy_json = '{"key1": "Word1 word2", "key2": "word2 word3"}'

    def test_ok_with_default_params(self):
        keyword_callback_mock = mock.Mock()

        parse_json(self.dummy_json, keyword_callback_mock)

        self.assertEqual(keyword_callback_mock.call_count, 4)

    def test_ok_with_spec_keywords(self):
        keywords = ["word2"]
        keyword_callback_mock = mock.Mock()

        parse_json(self.dummy_json, keyword_callback_mock, keywords=keywords)
        expected_calls = [
            mock.call("word2"),
            mock.call("word2")
        ]
        self.assertEqual(expected_calls, keyword_callback_mock.mock_calls)
        self.assertEqual(keyword_callback_mock.call_count, 2)

    def test_ok_with_spec_parameters(self):
        keywords = ["word2"]
        required_fields = ["key1"]
        keyword_callback_mock = mock.Mock()

        parse_json(self.dummy_json, keyword_callback_mock,
                   required_fields, keywords)
        self.assertEqual(keyword_callback_mock.call_count, 1)

    def test_ok_with_invalid_keywords(self):
        keywords = ["word4"]
        required_fields = ["key1", "key2"]
        keyword_callback_mock = mock.Mock()

        parse_json(self.dummy_json, keyword_callback_mock,
                   required_fields, keywords)
        self.assertEqual(keyword_callback_mock.call_count, 0)

    def test_ok_with_invalid_required_fields(self):
        keywords = ["word2"]
        required_fields = ["key3"]
        keyword_callback_mock = mock.Mock()
        with self.assertRaises(InvalidRequiredFieldError) as err:
            parse_json(self.dummy_json, keyword_callback_mock,
                       required_fields, keywords)

        self.assertEqual("invalid required field", str(err.exception))
        self.assertEqual(InvalidRequiredFieldError, type(err.exception))
        self.assertEqual(keyword_callback_mock.call_count, 0)
