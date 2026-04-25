from controller_app.model.topology import Topology
from controller_app.utils.json_utils import read_json_file, write_json_file


class TopologyDAO:
    def __init__(self, file_path="controller_app/data/topology.json"):
        self.file_path = file_path

    def load(self):
        data = read_json_file(self.file_path, {"links": []})
        return Topology.from_dict(data)

    def save(self, topology):
        write_json_file(self.file_path, topology.to_dict())

    def add_or_update_link(self, source_router, destination_router, cost):
        topology = self.load()
        topology.add_or_update_link(source_router, destination_router, cost)
        self.save(topology)
        return topology
