from router_app.utils.json_utils import read_json_file, write_json_file
from router_app.utils.logger import current_timestamp


class LogDAO:
    def __init__(self, file_path="router_app/data/logs.json"):
        self.file_path = file_path

    def add(self, event_type, message):
        logs = read_json_file(self.file_path, [])
        logs.append({
            "timestamp": current_timestamp(),
            "event_type": event_type,
            "message": message
        })
        write_json_file(self.file_path, logs)
