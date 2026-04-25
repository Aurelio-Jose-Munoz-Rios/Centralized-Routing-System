class RoutingController:
    def __init__(self, topology_service, routing_table_service, routing_table_dao, log_dao):
        self.topology_service = topology_service
        self.routing_table_service = routing_table_service
        self.routing_table_dao = routing_table_dao
        self.log_dao = log_dao

    def compute_and_save_all_tables(self):
        graph = self.topology_service.get_graph()
        routing_tables = self.routing_table_service.generate_all_tables(graph)
        self.routing_table_dao.save_all(routing_tables)
        self.log_dao.add("ROUTE_COMPUTATION", f"Generated {len(routing_tables)} routing tables")
        return routing_tables

    def get_table(self, router_id):
        return self.routing_table_dao.find_by_router_id(router_id)

    def get_all_tables(self):
        return self.routing_table_dao.find_all()
