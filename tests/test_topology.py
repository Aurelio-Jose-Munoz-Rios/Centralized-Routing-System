import unittest
from controller_app.model.topology import Topology


class TestTopology(unittest.TestCase):
    def test_add_or_update_link(self):
        topology = Topology()
        topology.add_or_update_link("R1", "R2", 10)
        topology.add_or_update_link("R2", "R1", 5)
        graph = topology.to_graph()

        self.assertEqual(len(topology.links), 1)
        self.assertEqual(graph["R1"]["R2"], 5)
        self.assertEqual(graph["R2"]["R1"], 5)


if __name__ == "__main__":
    unittest.main()
