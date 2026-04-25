from router_app.model.routing_table import RoutingTable
from router_app.model.routing_table_entry import RoutingTableEntry


class RoutingTableService:
    def __init__(self, message_service, controller_connection, routing_table_dao):
        self.message_service = message_service
        self.controller_connection = controller_connection
        self.routing_table_dao = routing_table_dao

    def request_table(self, router):
        message = self.message_service.build_get_table_message(router)
        response = self.controller_connection.send(message)
        self.save_table_from_response(router.router_id, response)
        return response

    def save_table_from_response(self, router_id, response):
        if response.get("type") != "ACK":
            return None

        entries = [RoutingTableEntry.from_dict(item) for item in response.get("routing_table", [])]
        routing_table = RoutingTable(router_id, entries)
        self.routing_table_dao.save(routing_table)
        return routing_table

    def load_local_table(self, router_id):
        return self.routing_table_dao.load(router_id)
