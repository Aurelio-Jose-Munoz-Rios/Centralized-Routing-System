class RouterCLIView:
    def display_welcome(self, router):
        print("=" * 70)
        print("      ROUTER APPLICATION CLI")
        print("=" * 70)
        print(f"Router ID: {router.router_id} | Hostname: {router.hostname}")
        print(f"Controller: {router.controller_ip}:{router.controller_port}")
        print("Type 'help' to see the available commands.")

    def get_command(self, router_id):
        return input(f"\n{router_id.lower()}-cli> ").strip()

    def show_help(self):
        print("\nAvailable commands:")
        print("  help")
        print("  register")
        print("  send topology")
        print("  request table")
        print("  show routing-table")
        print("  forward <destination_router>")
        print("  update cost <neighbor_router> <cost>")
        print("  exit")

    def show_message(self, message):
        print(f"[INFO] {message}")

    def show_error(self, message):
        print(f"[ERROR] {message}")

    def show_response(self, response):
        response_type = response.get("type", "UNKNOWN")
        message = response.get("message", "No message")
        print(f"[{response_type}] {message}")

        if "routing_table" in response:
            print(f"[INFO] Routing table entries received: {len(response['routing_table'])}")

    def show_routing_table(self, routing_table):
        if not routing_table or not routing_table.entries:
            self.show_message("Routing table is empty.")
            return

        print(f"\nRouting table for {routing_table.router_id}:")
        print("-" * 55)
        print(f"{'DESTINATION':<16}{'NEXT HOP':<16}{'COST':<10}")
        print("-" * 55)
        for entry in routing_table.entries:
            print(f"{entry.destination:<16}{entry.next_hop:<16}{entry.cost:<10}")
        print("-" * 55)

    def show_forwarding_decision(self, destination, entry):
        if entry:
            print(f"[FORWARD] Destination {destination} -> Next hop {entry.next_hop} | Cost {entry.cost}")
        else:
            self.show_error(f"No route found for destination {destination}.")
