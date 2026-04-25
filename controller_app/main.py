import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from controller_app.controller.communication_controller import CommunicationController
from controller_app.controller.controller_app_controller import ControllerAppController
from controller_app.controller.router_registry_controller import RouterRegistryController
from controller_app.controller.routing_controller import RoutingController
from controller_app.controller.topology_controller import TopologyController
from controller_app.dao.log_dao import LogDAO
from controller_app.dao.router_dao import RouterDAO
from controller_app.dao.routing_table_dao import RoutingTableDAO
from controller_app.dao.topology_dao import TopologyDAO
from controller_app.services.dijkstra_service import DijkstraService
from controller_app.services.message_service import MessageService
from controller_app.services.routing_table_service import RoutingTableService
from controller_app.services.topology_service import TopologyService
from controller_app.utils.config_loader import load_config
from controller_app.views.controller_cli_view import ControllerCLIView


def main():
    try:
        config = load_config("controller_app/config/controller_config.json")
        data_dir = config.get("data_dir", "controller_app/data")

        router_dao = RouterDAO(f"{data_dir}/routers.json")
        topology_dao = TopologyDAO(f"{data_dir}/topology.json")
        routing_table_dao = RoutingTableDAO(f"{data_dir}/routing_tables.json")
        log_dao = LogDAO(f"{data_dir}/logs.json")

        message_service = MessageService()
        topology_service = TopologyService(topology_dao)
        dijkstra_service = DijkstraService()
        routing_table_service = RoutingTableService(dijkstra_service)

        registry_controller = RouterRegistryController(router_dao, log_dao)
        topology_controller = TopologyController(topology_service, log_dao)
        routing_controller = RoutingController(topology_service, routing_table_service, routing_table_dao, log_dao)
        communication_controller = CommunicationController(
            message_service,
            registry_controller,
            topology_controller,
            routing_controller,
            log_dao
        )

        view = ControllerCLIView()
        app_controller = ControllerAppController(
            config,
            communication_controller,
            registry_controller,
            topology_controller,
            routing_controller,
            log_dao,
            view
        )

        app_controller.start_server()
        view.display_welcome(config["host"], config["port"])

        while True:
            command = view.get_command()
            if command == "exit":
                view.show_message("Closing controller. Goodbye.")
                app_controller.stop_server()
                break
            app_controller.execute_command(command)

    except Exception as exc:
        print(f"[FATAL ERROR] {exc}")


if __name__ == "__main__":
    main()
