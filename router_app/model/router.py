class Router:
    def __init__(self, router_id, hostname, ip, port, controller_ip, controller_port, neighbors=None):
        self.router_id = router_id
        self.hostname = hostname
        self.ip = ip
        self.port = int(port)
        self.controller_ip = controller_ip
        self.controller_port = int(controller_port)
        self.neighbors = neighbors or []

    @staticmethod
    def from_dict(data):
        return Router(
            data["router_id"],
            data.get("hostname", data["router_id"]),
            data["ip"],
            data["port"],
            data["controller_ip"],
            data["controller_port"],
            data.get("neighbors", [])
        )

    def to_dict(self):
        return {
            "router_id": self.router_id,
            "hostname": self.hostname,
            "ip": self.ip,
            "port": self.port,
            "controller_ip": self.controller_ip,
            "controller_port": self.controller_port,
            "neighbors": self.neighbors
        }
