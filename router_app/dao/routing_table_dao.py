from router_app.model.routing_table import RoutingTable
from router_app.utils.json_utils import read_json_file, write_json_file


class RoutingTableDAO:
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, routing_table):
        write_json_file(self.file_path, routing_table.to_dict())

    def load(self, router_id):
        data = read_json_file(self.file_path, {"router_id": router_id, "entries": []})
        return RoutingTable.from_dict(data)
