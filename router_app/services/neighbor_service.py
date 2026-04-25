class NeighborService:
    def __init__(self, message_service, controller_connection, neighbor_dao):
        self.message_service = message_service
        self.controller_connection = controller_connection
        self.neighbor_dao = neighbor_dao

    def send_topology(self, router):
        message = self.message_service.build_topology_message(router)
        return self.controller_connection.send(message)

    def update_neighbor_cost(self, router, neighbor_id, cost):
        self.neighbor_dao.update_cost(neighbor_id, cost)
        message = self.message_service.build_link_cost_update_message(router, neighbor_id, cost)
        return self.controller_connection.send(message)
