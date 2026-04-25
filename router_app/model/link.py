class Link:
    def __init__(self, source_router, destination_router, cost):
        self.source_router = source_router
        self.destination_router = destination_router
        self.cost = float(cost)
