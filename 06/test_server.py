import argparse
import socket
import time
from unittest import TestCase
from unittest import mock
import threading

from server import Server


class TestServer(TestCase):
    def setUp(self):
        args = argparse.Namespace(k=7, w=10)
        self.server = Server(socket.gethostname(), 8080, args)
        self.server_start = self.server.start()

    def tearDown(self):
        self.server.close()

    def test_server_is_working(self):
        with mock.patch("server.get_common_words") as mock_fetch:
            mock_fetch.return_value = {"в": 330, "и": 265, "—": 204, "//": 204, "для": 140, "{": 133, "не": 131}

            url = "https://habr.com/ru/articles/658623/"
            server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_sock.connect((socket.gethostname(), 8080))
            server_sock.send(url.encode())
            response = server_sock.recv(1024).decode()
            server_sock.close()

            self.assertEqual(response, '{"в": 330, "и": 265, "—": 204, "//": 204, "для": 140, "{": 133, "не": 131}')
            expected_calls = [
                mock.call(7, "https://habr.com/ru/articles/658623/"),
            ]
            self.assertEqual(expected_calls, mock_fetch.mock_calls)

    def test_server_is_working_multi(self):
        mutex = threading.Lock()
        responses = []

        def send_request(url):
            server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_sock.connect((socket.gethostname(), 8080))
            server_sock.send(url.encode())
            response = server_sock.recv(1024).decode()
            server_sock.close()
            with mutex:
                responses.append(response)

        with mock.patch("server.get_common_words") as mock_fetch:
            res = ['{"в": 336, "и": 265, "—": 204, "//": 204, "для": 140, "{": 133, "не": 131}',
                   '{"Хабр": 3, "Страница": 2, "не": 2, "Меню": 1, "β": 1, "Поиск": 1, "Профиль": 1}',
                   '{"и": 12, "на": 11, "с": 9, "в": 7, "к": 6, "для": 6, "ноутбуку": 5}']

            mock_fetch.side_effect = [{"в": 336, "и": 265, "—": 204, "//": 204, "для": 140, "{": 133, "не": 131},
                                      {"Хабр": 3, "Страница": 2, "не": 2, "Меню": 1, "β": 1, "Поиск": 1, "Профиль": 1},
                                      {"и": 12, "на": 11, "с": 9, "в": 7, "к": 6, "для": 6, "ноутбуку": 5}]

            urls = ["https://habr.com/ru/articles/658623/", "https://habr.com/ru/articles/658624/",
                    "https://habr.com/ru/articles/658625/"]
            for url in urls:
                thread = threading.Thread(target=send_request, args=(url,))
                thread.start()
            time.sleep(1)

            for resp in responses:
                self.assertIn(resp, res)

            self.assertEqual(mock_fetch.call_count, 3)
