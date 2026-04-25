import unittest
from controller_app.services.dijkstra_service import DijkstraService
from controller_app.services.routing_table_service import RoutingTableService


class TestRoutingTableService(unittest.TestCase):
    def test_generate_table_for_router(self):
        graph = {
            "R1": {"R2": 2, "R3": 5},
            "R2": {"R1": 2, "R3": 1, "R4": 4},
            "R3": {"R1": 5, "R2": 1, "R4": 3},
            "R4": {"R2": 4, "R3": 3}
        }
        service = RoutingTableService(DijkstraService())
        table = service.generate_table_for_router(graph, "R1")
        entries = {entry.destination: entry for entry in table.entries}

        self.assertEqual(entries["R3"].next_hop, "R2")
        self.assertEqual(entries["R3"].cost, 3)
        self.assertEqual(entries["R4"].next_hop, "R2")
        self.assertEqual(entries["R4"].cost, 6)


if __name__ == "__main__":
    unittest.main()
