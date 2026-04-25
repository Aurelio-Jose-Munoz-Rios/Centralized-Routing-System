class RoutingTable:
    def __init__(self, router_id, entries=None):
        self.router_id = router_id
        self.entries = entries or []

    @staticmethod
    def from_dict(data):
        from router_app.model.routing_table_entry import RoutingTableEntry
        entries = [RoutingTableEntry.from_dict(item) for item in data.get("entries", [])]
        return RoutingTable(data["router_id"], entries)

    def to_dict(self):
        return {
            "router_id": self.router_id,
            "entries": [entry.to_dict() for entry in self.entries]
        }
