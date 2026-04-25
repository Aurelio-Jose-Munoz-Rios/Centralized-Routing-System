class RouterAppController:
    def __init__(self, router, registration_controller, neighbor_controller, routing_table_controller, view):
        self.router = router
        self.registration_controller = registration_controller
        self.neighbor_controller = neighbor_controller
        self.routing_table_controller = routing_table_controller
        self.view = view

    def execute_command(self, command):
        if command == "help":
            self.view.show_help()

        elif command == "register":
            self.registration_controller.register(self.router)

        elif command == "send topology":
            self.neighbor_controller.send_topology(self.router)

        elif command == "request table":
            self.routing_table_controller.request_table(self.router)

        elif command == "show routing-table":
            self.routing_table_controller.show_local_table(self.router)

        elif command.startswith("forward "):
            parts = command.split()
            if len(parts) == 2:
                self.routing_table_controller.forward(self.router, parts[1])
            else:
                self.view.show_error("Invalid command. Use: forward <destination_router>")

        elif command.startswith("update cost "):
            parts = command.split()
            if len(parts) == 4:
                self.neighbor_controller.update_neighbor_cost(self.router, parts[2], parts[3])
            else:
                self.view.show_error("Invalid command. Use: update cost <neighbor_router> <cost>")

        else:
            self.view.show_error("Unknown command. Type 'help' to see available commands.")
