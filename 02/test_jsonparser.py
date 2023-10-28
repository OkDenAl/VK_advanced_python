import unittest
from unittest import mock
from jsonparser import parse_json
from jsonparser import KeywordsIsNoneError, KeywordCallbackIsNoneError, RequiredFieldsIsNoneError


class TestJsonParser(unittest.TestCase):
    def setUp(self):
        self.dummy_json = '{"key1": "Word1 word2 кактусовый", "key2": "word2 word3 word4 word4"}'

    def test_ok_with_spec_keywords_and_multi_params(self):
        keywords = ["word2"]
        required_fields = ["key1","key2"]
        keyword_callback_mock = mock.Mock()

        parse_json(self.dummy_json, keyword_callback_mock,required_fields,keywords)
        expected_calls = [
            mock.call("key1","word2"),
            mock.call("key2","word2")
        ]
        self.assertEqual(expected_calls, keyword_callback_mock.mock_calls)

    def test_ok_with_spec_parameters_and_multi_keys(self):
        keywords = ["word2","Word1"]
        required_fields = ["key1"]
        keyword_callback_mock = mock.Mock()

        parse_json(self.dummy_json, keyword_callback_mock,
                   required_fields, keywords)
        expected_calls = [
            mock.call("key1","word2"),
            mock.call("key1", "Word1"),
        ]
        self.assertEqual(expected_calls, keyword_callback_mock.mock_calls)

    def test_ok_with_no_kewords_match(self):
        keywords = ["word5","word6"]
        required_fields = ["key1", "key2"]
        keyword_callback_mock = mock.Mock()

        parse_json(self.dummy_json, keyword_callback_mock,
                   required_fields, keywords)
        self.assertEqual(keyword_callback_mock.call_count, 0)

    def test_ok_with_invalid_required_fields(self):
        keywords = ["word2"]
        required_fields = ["key3"]
        keyword_callback_mock = mock.Mock()
        parse_json(self.dummy_json, keyword_callback_mock,
                   required_fields, keywords)
        self.assertEqual(keyword_callback_mock.call_count, 0)

    def test_ok_with_different_register(self):
        keywords = ["WORD1"]
        required_fields = ["KEY1"]
        keyword_callback_mock = mock.Mock()
        parse_json(self.dummy_json, keyword_callback_mock,
                   required_fields, keywords)
        expected_calls = [
            mock.call("KEY1","WORD1"),
        ]
        self.assertEqual(expected_calls, keyword_callback_mock.mock_calls)

    def test_ok_find_only_full_words(self):
        keywords = ["кактус","word","Word2"]
        required_fields = ["key1"]
        keyword_callback_mock = mock.Mock()
        parse_json(self.dummy_json, keyword_callback_mock,
                   required_fields, keywords)
        expected_calls = [
            mock.call("key1","Word2"),
        ]
        self.assertEqual(expected_calls, keyword_callback_mock.mock_calls)

    def test_find_equal_words(self):
        keywords = ["word4","Word4"]
        required_fields = ["key2"]
        keyword_callback_mock = mock.Mock()
        parse_json(self.dummy_json, keyword_callback_mock,
                   required_fields, keywords)
        expected_calls = [
            mock.call("key2","word4"),
            mock.call("key2", "word4"),
            mock.call("key2", "Word4"),
            mock.call("key2", "Word4"),
        ]
        self.assertEqual(expected_calls, keyword_callback_mock.mock_calls)

    def test_find_multi(self):
        keywords = ["word3","word1"]
        required_fields = ["key1","key2"]
        keyword_callback_mock = mock.Mock()
        parse_json(self.dummy_json, keyword_callback_mock,
                   required_fields, keywords)
        expected_calls = [
            mock.call("key1","word1"),
            mock.call("key2", "word3"),
        ]
        self.assertEqual(expected_calls, keyword_callback_mock.mock_calls)


    def test_no_required_fields(self):
        keywords = ["word3","word1"]
        keyword_callback_mock = mock.Mock()
        with self.assertRaises(RequiredFieldsIsNoneError) as err:
            parse_json(self.dummy_json, keyword_callback_mock,keywords=keywords)

        self.assertEqual(RequiredFieldsIsNoneError, type(err.exception))

    def test_no_keywords(self):
        required_fields = ["key1", "key2"]
        keyword_callback_mock = mock.Mock()
        with self.assertRaises(KeywordsIsNoneError) as err:
            parse_json(self.dummy_json, keyword_callback_mock,required_fields)

        self.assertEqual(KeywordsIsNoneError, type(err.exception))

    def test_no_keyword_callback(self):
        keywords = ["word3", "word1"]
        required_fields = ["key1", "key2"]
        with self.assertRaises(KeywordCallbackIsNoneError) as err:
            parse_json(self.dummy_json, None,
                       required_fields, keywords)

        self.assertEqual(KeywordCallbackIsNoneError, type(err.exception))

