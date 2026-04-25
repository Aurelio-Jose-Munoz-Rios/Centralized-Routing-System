import socket
from router_app.utils.json_utils import encode_message, decode_message


class TCPClient:
    def __init__(self, host, port, timeout=5):
        self.host = host
        self.port = int(port)
        self.timeout = timeout

    def send_message(self, message):
        with socket.create_connection((self.host, self.port), timeout=self.timeout) as sock:
            stream = sock.makefile("rwb")
            stream.write(encode_message(message))
            stream.flush()
            raw_line = stream.readline()
            return decode_message(raw_line)
