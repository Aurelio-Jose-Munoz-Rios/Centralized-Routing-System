# Network Layer Notes Applied to the Project

This project applies several network-layer concepts from the data plane chapter.

## Forwarding vs Routing

- **Routing** determines the complete path from source to destination. In this project, routing is performed by the controller with Dijkstra.
- **Forwarding** moves a packet to the correct next hop. In this project, the router uses its routing table to select the next hop.

## Control Plane vs Data Plane

- The controller works as the **control plane** because it has network-wide logic.
- The router apps work as the **data plane** because they make local forwarding decisions using installed routing tables.

## SDN Inspiration

The project follows the simplified idea of Software-Defined Networking: a central controller computes and distributes forwarding information to routers.

## Best-Effort Model

The simulator does not guarantee delay, delivery or bandwidth. It only computes logical routing tables. This is similar to the Internet best-effort service model.

## Match + Action

The routing table is a simplified form of match + action:

- Match: destination router ID.
- Action: forward to next hop.

## Link Costs

Each link has a cost. Lower total cost paths are preferred by Dijkstra. This simulates route optimization in packet-switched networks.
