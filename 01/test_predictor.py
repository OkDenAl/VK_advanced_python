import unittest
from unittest import mock

from model import Model
from predictor import predict_message_mood
from predictor import ThresholdError


class TestPredictor(unittest.TestCase):
    def setUp(self):
        self.model = Model()

    def test_predict_good_mood(self):
        with mock.patch("model.Model.predict") as mock_fetch:
            mock_fetch.return_value = 0.8

            self.assertEqual("отл",
                             predict_message_mood("test", self.model, 0.1, 0.6))
            expected_calls = [
                mock.call("test"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_predict_good_mood_1(self):
        with mock.patch("model.Model.predict") as mock_fetch:
            mock_fetch.return_value = 1.0

            self.assertEqual("отл",
                             predict_message_mood("test", self.model, 0.999999, 1.0))
            expected_calls = [
                mock.call("test"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_predict_good_mood_edge(self):
        with mock.patch("model.Model.predict") as mock_fetch:
            mock_fetch.return_value = 0.3001

            self.assertEqual("отл",
                             predict_message_mood("test", self.model, 0.300001, 0.3001))
            expected_calls = [
                mock.call("test"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_predict_middle_mood(self):
        with mock.patch("model.Model.predict") as mock_fetch:
            mock_fetch.return_value = 0.30001

            self.assertEqual("норм",
                             predict_message_mood("test", self.model, 0.3000000001, 0.8))
            expected_calls = [
                mock.call("test"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_predict_middle_mood_edge(self):
        with mock.patch("model.Model.predict") as mock_fetch:
            mock_fetch.return_value = 0.30001

            self.assertEqual("норм",
                             predict_message_mood("test", self.model, 0.3000000001, 0.3001))
            expected_calls = [
                mock.call("test"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_predict_bad_mood(self):
        with mock.patch("model.Model.predict") as mock_fetch:
            mock_fetch.return_value = 0.299999

            self.assertEqual("неуд",
                             predict_message_mood("test", self.model, 0.3, 0.9))
            expected_calls = [
                mock.call("test"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_predict_bad_mood_0(self):
        with mock.patch("model.Model.predict") as mock_fetch:
            mock_fetch.return_value = 0.0

            self.assertEqual("неуд",
                             predict_message_mood("test", self.model, 0.0, 0.00000001))
            expected_calls = [
                mock.call("test"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_predict_bad_mood_edge(self):
        with mock.patch("model.Model.predict") as mock_fetch:
            mock_fetch.return_value = 0.3001

            self.assertEqual("неуд",
                             predict_message_mood("test", self.model, 0.3001, 0.301))
            expected_calls = [
                mock.call("test"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_predict_bad_equal_good(self):
        with mock.patch("model.Model.predict") as mock_fetch:
            mock_fetch.return_value = 0.8

            self.assertEqual("неуд",
                             predict_message_mood("test", self.model, 0.8, 0.8))
            expected_calls = [
                mock.call("test"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_predict_invalid_thresholds_bad_greater_then_good(self):
        with self.assertRaises(ThresholdError) as err:
            predict_message_mood("test", self.model, 0.81, 0.8)

        self.assertEqual("invalid thresholds", str(err.exception))
        self.assertEqual(ThresholdError, type(err.exception))

    def test_predict_invalid_thresholds_bad_less_then_0(self):
        with self.assertRaises(ThresholdError) as err:
            predict_message_mood("test", self.model, -0.1, 0.8)

        self.assertEqual("invalid thresholds", str(err.exception))
        self.assertEqual(ThresholdError, type(err.exception))

    def test_predict_invalid_thresholds_good_greater_then_1(self):
        with self.assertRaises(ThresholdError) as err:
            predict_message_mood("test", self.model, 0.1, 1.00001)

        self.assertEqual("invalid thresholds", str(err.exception))
        self.assertEqual(ThresholdError, type(err.exception))

    def test_predict_edge_case_predict_equal_bad_th(self):
        with mock.patch("model.Model.predict") as mock_fetch:
            mock_fetch.return_value = 0.4

            self.assertEqual("неуд",
                             predict_message_mood("test", self.model, 0.4, 0.8))
            expected_calls = [
                mock.call("test"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_predict_edge_predict_equal_good_th(self):
        with mock.patch("model.Model.predict") as mock_fetch:
            mock_fetch.return_value = 0.8

            self.assertEqual("отл",
                             predict_message_mood("test", self.model, 0.4, 0.8))
            expected_calls = [
                mock.call("test"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_predict_edge_case_predict_equal_0(self):
        with mock.patch("model.Model.predict") as mock_fetch:
            mock_fetch.return_value = 0

            self.assertEqual("неуд",
                             predict_message_mood("test", self.model, 0.4, 0.8))
            expected_calls = [
                mock.call("test"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)
    def test_predict_edge_predict_equal_1(self):
        with mock.patch("model.Model.predict") as mock_fetch:
            mock_fetch.return_value = 1

            self.assertEqual("отл",
                             predict_message_mood("test", self.model, 0.4, 0.8))
            expected_calls = [
                mock.call("test"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)
