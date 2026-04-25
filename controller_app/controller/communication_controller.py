class CommunicationController:
    def __init__(self, message_service, registry_controller, topology_controller, routing_controller, log_dao):
        self.message_service = message_service
        self.registry_controller = registry_controller
        self.topology_controller = topology_controller
        self.routing_controller = routing_controller
        self.log_dao = log_dao

    def handle_message(self, message):
        try:
            message_type = message.get("type")

            if message_type == "REGISTER_ROUTER":
                return self._handle_register_router(message)

            if message_type == "TOPOLOGY_UPDATE":
                return self._handle_topology_update(message)

            if message_type == "GET_ROUTING_TABLE":
                return self._handle_get_routing_table(message)

            if message_type == "LINK_COST_UPDATE":
                return self._handle_link_cost_update(message)

            if message_type == "PING":
                return self.message_service.ack("Controller is alive.")

            return self.message_service.error(f"Unknown message type: {message_type}")
        except Exception as exc:
            self.log_dao.add("ERROR", str(exc))
            return self.message_service.error(str(exc))

    def _handle_register_router(self, message):
        self.message_service.require_fields(message, ["router_id", "ip", "port"])
        router = self.registry_controller.register_router(message["router_id"], message["ip"], message["port"])
        return self.message_service.ack("Router registered successfully.", {"router": router.to_dict()})

    def _handle_topology_update(self, message):
        self.message_service.require_fields(message, ["router_id", "neighbors"])
        router_id = message["router_id"]
        self.topology_controller.update_neighbors(router_id, message["neighbors"])
        self.routing_controller.compute_and_save_all_tables()
        routing_table = self.routing_controller.get_table(router_id)
        table_entries = [entry.to_dict() for entry in routing_table.entries] if routing_table else []
        return self.message_service.ack("Topology updated and routing table generated.", {
            "router_id": router_id,
            "routing_table": table_entries
        })

    def _handle_get_routing_table(self, message):
        self.message_service.require_fields(message, ["router_id"])
        router_id = message["router_id"]
        routing_table = self.routing_controller.get_table(router_id)
        table_entries = [entry.to_dict() for entry in routing_table.entries] if routing_table else []
        return self.message_service.ack("Routing table retrieved.", {
            "router_id": router_id,
            "routing_table": table_entries
        })

    def _handle_link_cost_update(self, message):
        self.message_service.require_fields(message, ["source_router", "destination_router", "cost"])
        self.topology_controller.update_link_cost(
            message["source_router"],
            message["destination_router"],
            message["cost"]
        )
        self.routing_controller.compute_and_save_all_tables()
        router_id = message.get("router_id", message["source_router"])
        routing_table = self.routing_controller.get_table(router_id)
        table_entries = [entry.to_dict() for entry in routing_table.entries] if routing_table else []
        return self.message_service.ack("Link cost updated and routes recalculated.", {
            "router_id": router_id,
            "routing_table": table_entries
        })
