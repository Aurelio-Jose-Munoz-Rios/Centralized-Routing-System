class ControllerCLIView:
    def display_welcome(self, host, port):
        print("=" * 70)
        print("      CENTRALIZED ROUTING CONTROLLER")
        print("=" * 70)
        print(f"Controller listening on {host}:{port}")
        print("Type 'help' to see the available commands.")

    def get_command(self):
        return input("\ncontroller-cli> ").strip()

    def show_help(self):
        print("\nAvailable commands:")
        print("  help")
        print("  show routers")
        print("  show topology")
        print("  show table <router_id>")
        print("  show tables")
        print("  compute routes")
        print("  update cost <source_router> <destination_router> <cost>")
        print("  show logs")
        print("  exit")

    def show_message(self, message):
        print(f"[INFO] {message}")

    def show_error(self, message):
        print(f"[ERROR] {message}")

    def show_routers(self, routers):
        if not routers:
            self.show_message("No registered routers found.")
            return

        print("\nRegistered routers:")
        print("-" * 88)
        print(f"{'ID':<10}{'IP':<18}{'PORT':<8}{'STATUS':<12}{'LAST SEEN':<22}")
        print("-" * 88)
        for router in routers:
            print(f"{router.router_id:<10}{router.ip:<18}{router.port:<8}{router.status:<12}{router.last_seen:<22}")
        print("-" * 88)

    def show_topology(self, topology):
        if not topology.links:
            self.show_message("Topology is empty.")
            return

        print("\nNetwork topology:")
        print("-" * 50)
        print(f"{'SOURCE':<12}{'DESTINATION':<16}{'COST':<10}")
        print("-" * 50)
        for link in topology.links:
            print(f"{link.source_router:<12}{link.destination_router:<16}{link.cost:<10}")
        print("-" * 50)

    def show_routing_table(self, routing_table):
        if not routing_table:
            self.show_message("Routing table not found.")
            return

        print(f"\nRouting table for {routing_table.router_id}:")
        print("-" * 55)
        print(f"{'DESTINATION':<16}{'NEXT HOP':<16}{'COST':<10}")
        print("-" * 55)
        for entry in routing_table.entries:
            print(f"{entry.destination:<16}{entry.next_hop:<16}{entry.cost:<10}")
        print("-" * 55)

    def show_all_tables(self, routing_tables):
        if not routing_tables:
            self.show_message("No routing tables found.")
            return

        for routing_table in routing_tables:
            self.show_routing_table(routing_table)

    def show_logs(self, logs):
        if not logs:
            self.show_message("No logs found.")
            return

        print("\nSystem logs:")
        print("-" * 95)
        print(f"{'TIMESTAMP':<22}{'TYPE':<20}{'MESSAGE':<50}")
        print("-" * 95)
        for item in logs[-20:]:
            print(f"{item['timestamp']:<22}{item['event_type']:<20}{item['message']:<50}")
        print("-" * 95)
