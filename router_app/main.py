import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from router_app.controller.neighbor_controller import NeighborController
from router_app.controller.registration_controller import RegistrationController
from router_app.controller.router_app_controller import RouterAppController
from router_app.controller.routing_table_controller import RoutingTableController
from router_app.dao.log_dao import LogDAO
from router_app.dao.neighbor_dao import NeighborDAO
from router_app.dao.router_config_dao import RouterConfigDAO
from router_app.dao.routing_table_dao import RoutingTableDAO
from router_app.network.controller_connection import ControllerConnection
from router_app.services.forwarding_service import ForwardingService
from router_app.services.message_service import MessageService
from router_app.services.neighbor_service import NeighborService
from router_app.services.registration_service import RegistrationService
from router_app.services.routing_table_service import RoutingTableService
from router_app.views.router_cli_view import RouterCLIView


def main():
    try:
        config_path = sys.argv[1] if len(sys.argv) > 1 else "router_app/config/router_R1.json"

        config_dao = RouterConfigDAO(config_path)
        router = config_dao.load_router()

        routing_table_path = f"router_app/data/routing_table_{router.router_id}.json"
        neighbor_dao = NeighborDAO(router)
        routing_table_dao = RoutingTableDAO(routing_table_path)
        log_dao = LogDAO("router_app/data/logs.json")

        view = RouterCLIView()
        controller_connection = ControllerConnection(router)
        message_service = MessageService()
        forwarding_service = ForwardingService()

        registration_service = RegistrationService(message_service, controller_connection)
        neighbor_service = NeighborService(message_service, controller_connection, neighbor_dao)
        routing_table_service = RoutingTableService(message_service, controller_connection, routing_table_dao)

        registration_controller = RegistrationController(registration_service, view, log_dao)
        neighbor_controller = NeighborController(neighbor_service, routing_table_service, view, log_dao)
        routing_table_controller = RoutingTableController(routing_table_service, forwarding_service, view)

        app_controller = RouterAppController(router, registration_controller, neighbor_controller, routing_table_controller, view)

        view.display_welcome(router)

        while True:
            command = view.get_command(router.router_id)
            if command == "exit":
                view.show_message("Closing router CLI. Goodbye.")
                break
            app_controller.execute_command(command)

    except Exception as exc:
        print(f"[FATAL ERROR] {exc}")


if __name__ == "__main__":
    main()
