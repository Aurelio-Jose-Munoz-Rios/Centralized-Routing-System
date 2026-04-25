class RoutingTableView:
    def show(self, routing_table):
        if routing_table:
            for entry in routing_table.entries:
                print(entry)
