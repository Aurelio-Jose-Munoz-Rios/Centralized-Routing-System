import heapq


class DijkstraService:
    def compute_shortest_paths(self, graph, source_router):
        distances = {router_id: float("inf") for router_id in graph}
        previous = {router_id: None for router_id in graph}

        if source_router not in graph:
            return distances, previous

        distances[source_router] = 0
        queue = [(0, source_router)]

        while queue:
            current_distance, current_router = heapq.heappop(queue)

            if current_distance > distances[current_router]:
                continue

            for neighbor, cost in graph[current_router].items():
                new_distance = current_distance + float(cost)
                if new_distance < distances.get(neighbor, float("inf")):
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_router
                    heapq.heappush(queue, (new_distance, neighbor))

        return distances, previous

    def build_path(self, previous, source_router, destination_router):
        path = []
        current = destination_router

        while current is not None:
            path.insert(0, current)
            if current == source_router:
                return path
            current = previous.get(current)

        return []
