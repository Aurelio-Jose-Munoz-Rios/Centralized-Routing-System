from controller_app.model.router import Router
from controller_app.utils.json_utils import read_json_file, write_json_file
from controller_app.utils.logger import current_timestamp


class RouterDAO:
    def __init__(self, file_path="controller_app/data/routers.json"):
        self.file_path = file_path

    def insert_or_update(self, router):
        routers = read_json_file(self.file_path, {})
        router.last_seen = current_timestamp()
        routers[router.router_id] = router.to_dict()
        write_json_file(self.file_path, routers)

    def find_by_id(self, router_id):
        routers = read_json_file(self.file_path, {})
        data = routers.get(router_id)
        return Router.from_dict(data) if data else None

    def find_all(self):
        routers = read_json_file(self.file_path, {})
        return [Router.from_dict(item) for item in routers.values()]

    def delete(self, router_id):
        routers = read_json_file(self.file_path, {})
        if router_id in routers:
            del routers[router_id]
            write_json_file(self.file_path, routers)
