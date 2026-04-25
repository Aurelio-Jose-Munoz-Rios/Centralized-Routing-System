class Neighbor:
    def __init__(self, neighbor_id, cost):
        self.neighbor_id = neighbor_id
        self.cost = float(cost)

    def to_dict(self):
        return {
            "neighbor_id": self.neighbor_id,
            "cost": self.cost
        }
