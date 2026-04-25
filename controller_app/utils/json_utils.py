import json
from pathlib import Path


def read_json_file(file_path, default_value):
    path = Path(file_path)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        write_json_file(path, default_value)
        return default_value

    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return default_value

    return json.loads(text)


def write_json_file(file_path, data):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def encode_message(message):
    return (json.dumps(message) + "\n").encode("utf-8")


def decode_message(raw_line):
    return json.loads(raw_line.decode("utf-8"))
