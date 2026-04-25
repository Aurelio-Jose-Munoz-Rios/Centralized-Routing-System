class NeighborDAO:
    def __init__(self, router):
        self.router = router

    def find_all(self):
        return self.router.neighbors

    def update_cost(self, neighbor_id, cost):
        for neighbor in self.router.neighbors:
            if neighbor["neighbor_id"] == neighbor_id:
                neighbor["cost"] = float(cost)
                return True
        self.router.neighbors.append({"neighbor_id": neighbor_id, "cost": float(cost)})
        return True
