from server import Server
from client import Client
import socket
from threading import Thread

response1 = None
response2 = None


def run_server():
    s = Server()  # Press Ctrl+F8 to toggle the breakpoint.
    s.bind_and_listen(" and here is the hi from server!", socket.gethostname(), 5000)


def run_client():
    c = Client()
    c.connect(socket.gethostname(), 5000)
    response1 = c.send_message("Hi 1 from client")
    response2 = c.send_message("Hi 2 from client!")
    assert response1 == "Hi 1 from client and here is the hi from server!"
    assert response2 == "Hi 2 from client! and here is the hi from server!"
    c.close_connection()


def test_send_message():
    p1 = Thread(target=run_server)
    p1.start()
    p2 = Thread(target=run_client)
    p2.start()
