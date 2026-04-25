class RoutingTableController:
    def __init__(self, routing_table_service, forwarding_service, view):
        self.routing_table_service = routing_table_service
        self.forwarding_service = forwarding_service
        self.view = view

    def request_table(self, router):
        response = self.routing_table_service.request_table(router)
        self.view.show_response(response)
        return response

    def show_local_table(self, router):
        routing_table = self.routing_table_service.load_local_table(router.router_id)
        self.view.show_routing_table(routing_table)

    def forward(self, router, destination):
        routing_table = self.routing_table_service.load_local_table(router.router_id)
        entry = self.forwarding_service.get_next_hop(routing_table, destination)
        self.view.show_forwarding_decision(destination, entry)
