class RoutingTableEntry:
    def __init__(self, destination, next_hop, cost):
        self.destination = destination
        self.next_hop = next_hop
        self.cost = float(cost)

    def to_dict(self):
        return {
            "destination": self.destination,
            "next_hop": self.next_hop,
            "cost": self.cost
        }

    @staticmethod
    def from_dict(data):
        return RoutingTableEntry(data["destination"], data["next_hop"], data["cost"])

    def __str__(self):
        return f"Destination: {self.destination} | Next hop: {self.next_hop} | Cost: {self.cost}"
