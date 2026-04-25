class Link:
    def __init__(self, source_router, destination_router, cost):
        self.source_router = source_router
        self.destination_router = destination_router
        self.cost = float(cost)

    def to_dict(self):
        return {
            "source_router": self.source_router,
            "destination_router": self.destination_router,
            "cost": self.cost
        }

    @staticmethod
    def from_dict(data):
        return Link(data["source_router"], data["destination_router"], data["cost"])

    def __str__(self):
        return f"{self.source_router} <-> {self.destination_router} | Cost: {self.cost}"
