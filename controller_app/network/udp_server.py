class UDPServer:
    def __init__(self, host, port, communication_controller):
        self.host = host
        self.port = int(port)
        self.communication_controller = communication_controller

    def start(self):
        raise NotImplementedError("UDP server is documented but TCP is the implemented protocol for this version.")
