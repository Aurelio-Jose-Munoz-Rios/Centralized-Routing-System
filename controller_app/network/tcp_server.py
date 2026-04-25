import socket
import threading
from controller_app.network.client_handler import ClientHandler


class TCPServer:
    def __init__(self, host, port, communication_controller):
        self.host = host
        self.port = int(port)
        self.communication_controller = communication_controller
        self.server_socket = None
        self.running = False

    def start(self):
        self.running = True
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(20)

        print(f"[INFO] Controller TCP server listening on {self.host}:{self.port}")

        while self.running:
            try:
                client_socket, address = self.server_socket.accept()
                handler = ClientHandler(client_socket, address, self.communication_controller)
                thread = threading.Thread(target=handler.handle, daemon=True)
                thread.start()
            except OSError:
                break

    def stop(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()
