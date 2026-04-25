from controller_app.model.routing_table import RoutingTable
from controller_app.model.routing_table_entry import RoutingTableEntry


class RoutingTableService:
    def __init__(self, dijkstra_service):
        self.dijkstra_service = dijkstra_service

    def generate_table_for_router(self, graph, router_id):
        distances, previous = self.dijkstra_service.compute_shortest_paths(graph, router_id)
        entries = []

        for destination in sorted(graph.keys()):
            if destination == router_id:
                continue

            cost = distances.get(destination, float("inf"))
            if cost == float("inf"):
                continue

            path = self.dijkstra_service.build_path(previous, router_id, destination)
            if len(path) < 2:
                continue

            next_hop = path[1]
            entries.append(RoutingTableEntry(destination, next_hop, cost))

        return RoutingTable(router_id, entries)

    def generate_all_tables(self, graph):
        return [self.generate_table_for_router(graph, router_id) for router_id in sorted(graph.keys())]
