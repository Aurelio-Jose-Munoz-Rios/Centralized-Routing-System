import threading
from controller_app.network.tcp_server import TCPServer


class ControllerAppController:
    def __init__(self, config, communication_controller, registry_controller, topology_controller, routing_controller, log_dao, view):
        self.config = config
        self.communication_controller = communication_controller
        self.registry_controller = registry_controller
        self.topology_controller = topology_controller
        self.routing_controller = routing_controller
        self.log_dao = log_dao
        self.view = view
        self.server = None

    def start_server(self):
        self.server = TCPServer(self.config["host"], self.config["port"], self.communication_controller)
        thread = threading.Thread(target=self.server.start, daemon=True)
        thread.start()

    def stop_server(self):
        if self.server:
            self.server.stop()

    def execute_command(self, command):
        if command == "help":
            self.view.show_help()

        elif command == "show routers":
            self.view.show_routers(self.registry_controller.list_routers())

        elif command == "show topology":
            self.view.show_topology(self.topology_controller.get_topology())

        elif command == "show tables":
            self.view.show_all_tables(self.routing_controller.get_all_tables())

        elif command.startswith("show table "):
            parts = command.split()
            if len(parts) == 3:
                self.view.show_routing_table(self.routing_controller.get_table(parts[2]))
            else:
                self.view.show_error("Invalid command. Use: show table <router_id>")

        elif command == "compute routes":
            tables = self.routing_controller.compute_and_save_all_tables()
            self.view.show_message(f"Generated {len(tables)} routing tables.")

        elif command.startswith("update cost "):
            self._execute_update_cost(command)

        elif command == "show logs":
            self.view.show_logs(self.log_dao.find_all())

        else:
            self.view.show_error("Unknown command. Type 'help' to see available commands.")

    def _execute_update_cost(self, command):
        parts = command.split()
        if len(parts) != 5:
            self.view.show_error("Invalid command. Use: update cost <source_router> <destination_router> <cost>")
            return

        source_router = parts[2]
        destination_router = parts[3]
        cost = parts[4]
        self.topology_controller.update_link_cost(source_router, destination_router, cost)
        self.routing_controller.compute_and_save_all_tables()
        self.view.show_message("Link cost updated and routes recalculated.")
