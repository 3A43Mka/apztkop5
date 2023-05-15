import socket


class Client:

    def __init__(self):
        self.client_socket = None

    def connect(self, host, port):
        self.client_socket = socket.socket()
        self.client_socket.connect((host, port))

    def send_message(self, msg):
        self.client_socket.send(msg.encode())
        return self.client_socket.recv(1024).decode()

    def close_connection(self):
        self.client_socket.close()
