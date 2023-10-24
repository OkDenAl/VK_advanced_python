import argparse
import json
import threading
import socket
from utils import get_common_words


class Server:
    def __init__(self, host, port, input_args):
        self.master = None
        self.host = host
        self.port = port
        self.workers = input_args.w
        self.top_words = input_args.k
        self.processed_urls = 0
        self.mutex = threading.Lock()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(self.workers)

    def listen_and_serve(self):
        while True:
            if threading.activeCount() - 1 < self.workers:
                try:
                    conn, _ = self.server_socket.accept()
                except OSError:
                    break
                thread = threading.Thread(target=self.handle_client, args=(conn,))
                thread.start()

    def start(self):
        self.master = threading.Thread(target=self.listen_and_serve, daemon=True)
        self.master.start()
        return self.master

    def handle_client(self, conn):
        msg = conn.recv(1024).decode().strip()
        most_common_words = get_common_words(self.top_words, msg)
        conn.send(json.dumps(most_common_words, ensure_ascii=False).encode())
        conn.close()
        with self.mutex:
            self.processed_urls += 1
        print(f'PROCESSED_URLS={self.processed_urls}')

    def close(self):
        if self.server_socket:
            self.server_socket.shutdown(socket.SHUT_RDWR)
            self.server_socket.close()


def create_parser():
    pars = argparse.ArgumentParser()
    pars.add_argument('-w', type=int, default='10', help="workers count")
    pars.add_argument('-k', type=int, default='7', help="most common words count")

    return pars


if __name__ == "__main__":
    parser = create_parser()
    console_args = parser.parse_args()
    server = Server(socket.gethostname(), 8080, console_args)

    master = threading.Thread(target=server.listen_and_serve, daemon=True)
    master.start()

    master.join()
