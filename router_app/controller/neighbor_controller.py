class NeighborController:
    def __init__(self, neighbor_service, routing_table_service, view, log_dao):
        self.neighbor_service = neighbor_service
        self.routing_table_service = routing_table_service
        self.view = view
        self.log_dao = log_dao

    def send_topology(self, router):
        response = self.neighbor_service.send_topology(router)
        self.routing_table_service.save_table_from_response(router.router_id, response)
        self.log_dao.add("TOPOLOGY_UPDATE", str(response))
        self.view.show_response(response)
        return response

    def update_neighbor_cost(self, router, neighbor_id, cost):
        response = self.neighbor_service.update_neighbor_cost(router, neighbor_id, cost)
        self.routing_table_service.save_table_from_response(router.router_id, response)
        self.log_dao.add("LINK_COST_UPDATE", str(response))
        self.view.show_response(response)
        return response
