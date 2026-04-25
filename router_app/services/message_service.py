class MessageService:
    def build_registration_message(self, router):
        return {
            "type": "REGISTER_ROUTER",
            "router_id": router.router_id,
            "ip": router.ip,
            "port": router.port
        }

    def build_topology_message(self, router):
        return {
            "type": "TOPOLOGY_UPDATE",
            "router_id": router.router_id,
            "neighbors": router.neighbors
        }

    def build_get_table_message(self, router):
        return {
            "type": "GET_ROUTING_TABLE",
            "router_id": router.router_id
        }

    def build_link_cost_update_message(self, router, destination_router, cost):
        return {
            "type": "LINK_COST_UPDATE",
            "router_id": router.router_id,
            "source_router": router.router_id,
            "destination_router": destination_router,
            "cost": float(cost)
        }
