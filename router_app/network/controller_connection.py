from router_app.network.tcp_client import TCPClient


class ControllerConnection:
    def __init__(self, router):
        self.router = router
        self.client = TCPClient(router.controller_ip, router.controller_port)

    def send(self, message):
        return self.client.send_message(message)
