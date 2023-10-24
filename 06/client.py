import argparse
import socket
import threading

IP = socket.gethostname()
PORT = 8080
ADDR = (IP, PORT)
SIZE = 1024


def create_parser():
    pars = argparse.ArgumentParser()
    pars.add_argument('-threads_count', type=int, default='10')
    pars.add_argument('-path_to_url_file', type=str, default='urls.txt')

    return pars


def send_request(url):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.connect(ADDR)
    server_sock.send(url.encode())
    response = server_sock.recv(1024).decode()
    server_sock.close()
    print(f'{str(url)} :{response}')


def start_client(input_args):
    with open(input_args.path_to_url_file, 'r') as file:
        while True:
            if threading.activeCount() - 1 < input_args.threads_count:
                url = file.readline().strip()
                if not url:
                    break
                thread = threading.Thread(target=send_request, args=(url,))
                thread.start()
                print(threading.activeCount() - 1)


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    start_client(args)
