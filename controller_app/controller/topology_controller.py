class TopologyController:
    def __init__(self, topology_service, log_dao):
        self.topology_service = topology_service
        self.log_dao = log_dao

    def update_neighbors(self, router_id, neighbors):
        topology = self.topology_service.update_neighbors(router_id, neighbors)
        self.log_dao.add("TOPOLOGY_UPDATE", f"Router {router_id} sent {len(neighbors)} neighbors")
        return topology

    def update_link_cost(self, source_router, destination_router, cost):
        topology = self.topology_service.update_link_cost(source_router, destination_router, cost)
        self.log_dao.add("LINK_COST_UPDATE", f"Updated {source_router}-{destination_router} cost to {cost}")
        return topology

    def get_topology(self):
        return self.topology_service.topology_dao.load()
