class TopologyView:
    def show(self, topology):
        for link in topology.links:
            print(link)
