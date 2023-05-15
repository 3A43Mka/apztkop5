import socket


class Server:
    def __init__(self):
        self.server_socket = None

    def bind_and_listen(self, data_from_server, host, port):
        self.server_socket = socket.socket()
        self.server_socket.bind((host, port))
        self.server_socket.listen(2)
        conn, address = self.server_socket.accept()
        print("Connection from: " + str(address))
        while True:
            data_from_client = conn.recv(1024).decode()
            if not data_from_client:
                break
            print("from connected user: " + str(data_from_client))
            data = f'{data_from_client}{data_from_server}'
            conn.send(data.encode())
        conn.close()
