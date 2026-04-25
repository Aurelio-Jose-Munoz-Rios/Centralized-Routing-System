class Router:
    def __init__(self, router_id, ip, port, status="ACTIVE", last_seen=""):
        self.router_id = router_id
        self.ip = ip
        self.port = int(port)
        self.status = status
        self.last_seen = last_seen

    def to_dict(self):
        return {
            "router_id": self.router_id,
            "ip": self.ip,
            "port": self.port,
            "status": self.status,
            "last_seen": self.last_seen
        }

    @staticmethod
    def from_dict(data):
        return Router(
            data["router_id"],
            data["ip"],
            data["port"],
            data.get("status", "ACTIVE"),
            data.get("last_seen", "")
        )

    def __str__(self):
        return (
            f"ID: {self.router_id} | IP: {self.ip} | Port: {self.port} | "
            f"Status: {self.status} | Last seen: {self.last_seen}"
        )
