class TopologyService:
    def __init__(self, topology_dao):
        self.topology_dao = topology_dao

    def update_neighbors(self, router_id, neighbors):
        topology = self.topology_dao.load()
        for neighbor in neighbors:
            topology.add_or_update_link(router_id, neighbor["neighbor_id"], neighbor["cost"])
        self.topology_dao.save(topology)
        return topology

    def update_link_cost(self, source_router, destination_router, cost):
        return self.topology_dao.add_or_update_link(source_router, destination_router, cost)

    def get_graph(self):
        return self.topology_dao.load().to_graph()
