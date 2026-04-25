import unittest
from controller_app.services.dijkstra_service import DijkstraService


class TestDijkstraService(unittest.TestCase):
    def test_shortest_path(self):
        graph = {
            "R1": {"R2": 2, "R3": 5},
            "R2": {"R1": 2, "R3": 1},
            "R3": {"R1": 5, "R2": 1}
        }
        service = DijkstraService()
        distances, previous = service.compute_shortest_paths(graph, "R1")
        path = service.build_path(previous, "R1", "R3")

        self.assertEqual(distances["R3"], 3)
        self.assertEqual(path, ["R1", "R2", "R3"])


if __name__ == "__main__":
    unittest.main()
