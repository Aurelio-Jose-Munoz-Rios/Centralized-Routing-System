from controller_app.utils.json_utils import encode_message, decode_message


class ClientHandler:
    def __init__(self, client_socket, address, communication_controller):
        self.client_socket = client_socket
        self.address = address
        self.communication_controller = communication_controller

    def handle(self):
        with self.client_socket:
            stream = self.client_socket.makefile("rwb")
            raw_line = stream.readline()
            if not raw_line:
                return

            try:
                message = decode_message(raw_line)
                response = self.communication_controller.handle_message(message)
            except Exception as exc:
                response = {
                    "type": "ERROR",
                    "message": f"Invalid JSON message: {exc}"
                }

            stream.write(encode_message(response))
            stream.flush()
