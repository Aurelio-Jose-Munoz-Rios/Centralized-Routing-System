import json
from pathlib import Path


def load_router_config(config_path):
    config_file = Path(config_path)
    return json.loads(config_file.read_text(encoding="utf-8"))
