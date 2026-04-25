from controller_app.model.routing_table import RoutingTable
from controller_app.utils.json_utils import read_json_file, write_json_file


class RoutingTableDAO:
    def __init__(self, file_path="controller_app/data/routing_tables.json"):
        self.file_path = file_path

    def save_table(self, routing_table):
        tables = read_json_file(self.file_path, {})
        tables[routing_table.router_id] = routing_table.to_dict()
        write_json_file(self.file_path, tables)

    def save_all(self, routing_tables):
        tables = {table.router_id: table.to_dict() for table in routing_tables}
        write_json_file(self.file_path, tables)

    def find_by_router_id(self, router_id):
        tables = read_json_file(self.file_path, {})
        data = tables.get(router_id)
        return RoutingTable.from_dict(data) if data else None

    def find_all(self):
        tables = read_json_file(self.file_path, {})
        return [RoutingTable.from_dict(item) for item in tables.values()]
