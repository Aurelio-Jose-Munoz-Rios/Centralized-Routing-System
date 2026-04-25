class ForwardingService:
    def get_next_hop(self, routing_table, destination):
        for entry in routing_table.entries:
            if entry.destination == destination:
                return entry
        return None
