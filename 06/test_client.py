import argparse
import socket
import time
from unittest import TestCase
from unittest import mock

from client import start_client


class TestClient(TestCase):
    def setUp(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((socket.gethostname(), 8080))
        self.server_socket.listen(5)

    def tearDown(self):
        self.server_socket.close()

    def test_multi_client_is_working(self):
        with mock.patch("socket.socket.recv") as mock_fetch:
            mock_fetch.return_value = b'answer'
            args = argparse.Namespace(threads_count=7, path_to_url_file='test_urls.txt')
            start_client(args)
            time.sleep(1)
            self.assertEqual(mock_fetch.call_count, 6)
