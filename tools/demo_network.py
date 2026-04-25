import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import json
import socket


def send_message(host, port, message):
    with socket.create_connection((host, port), timeout=5) as sock:
        stream = sock.makefile("rwb")
        stream.write((json.dumps(message) + "\n").encode("utf-8"))
        stream.flush()
        raw_line = stream.readline()
        return json.loads(raw_line.decode("utf-8"))


def load_router_configs():
    config_dir = Path("router_app/config")
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(config_dir.glob("router_R*.json"))]


def main():
    routers = load_router_configs()
    if not routers:
        print("No router configs found.")
        return

    controller_host = routers[0]["controller_ip"]
    controller_port = routers[0]["controller_port"]

    print("Registering routers...")
    for router in routers:
        response = send_message(controller_host, controller_port, {
            "type": "REGISTER_ROUTER",
            "router_id": router["router_id"],
            "ip": router["ip"],
            "port": router["port"]
        })
        print(router["router_id"], response.get("type"), response.get("message"))

    print("\nSending topology updates...")
    for router in routers:
        response = send_message(controller_host, controller_port, {
            "type": "TOPOLOGY_UPDATE",
            "router_id": router["router_id"],
            "neighbors": router["neighbors"]
        })
        print(router["router_id"], response.get("type"), response.get("message"))
        print("Routing table:", response.get("routing_table", []))

    print("\nDemo completed.")


if __name__ == "__main__":
    main()
