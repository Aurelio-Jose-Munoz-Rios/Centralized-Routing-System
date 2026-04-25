class Topology:
    def __init__(self, links=None):
        self.links = links or []

    def add_or_update_link(self, source_router, destination_router, cost):
        source_router = source_router.strip()
        destination_router = destination_router.strip()
        cost = float(cost)

        for link in self.links:
            same_direction = link.source_router == source_router and link.destination_router == destination_router
            inverse_direction = link.source_router == destination_router and link.destination_router == source_router
            if same_direction or inverse_direction:
                link.cost = cost
                return

        from controller_app.model.link import Link
        self.links.append(Link(source_router, destination_router, cost))

    def to_graph(self):
        graph = {}
        for link in self.links:
            graph.setdefault(link.source_router, {})[link.destination_router] = link.cost
            graph.setdefault(link.destination_router, {})[link.source_router] = link.cost
        return graph

    def to_dict(self):
        return {"links": [link.to_dict() for link in self.links]}

    @staticmethod
    def from_dict(data):
        from controller_app.model.link import Link
        links = [Link.from_dict(item) for item in data.get("links", [])]
        return Topology(links)
