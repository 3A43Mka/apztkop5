from server import Server
from client import Client
import socket
from threading import Thread


def run_server():
    s = Server()
    s.bind_and_listen(" and here is the hi from server!", socket.gethostname(), 5000)


def run_client():
    c = Client()
    c.connect(socket.gethostname(), 5000)
    print(c.send_message("Hi 1 from client"))
    print(c.send_message("Hi 2 from client!"))
    c.close_connection()


if __name__ == '__main__':
    p1 = Thread(target=run_server)
    p1.start()
    p2 = Thread(target=run_client)
    p2.start()
