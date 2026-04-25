# System Architecture

## Architectural Style

The system follows a centralized controller-based architecture, inspired by Software-Defined Networking at an educational level. Router applications send local topology information to the controller. The controller builds a global network view and computes forwarding information.

## Main Components

| Component | Main responsibility | Input | Output |
|---|---|---|---|
| Controller application | Manage global network state and compute routes | Router registration, topology updates, link cost updates | Routing tables, ACK messages, error messages |
| Router application | Represent a software router | Routing table from controller | Registration message, topology update, forwarding queries |
| Topology manager | Store the network topology | Nodes, links, costs | Graph or adjacency list |
| Routing algorithm module | Compute shortest paths | Network topology | Paths and costs |
| Routing table manager | Convert paths into routing table entries | Shortest paths | Destination, next hop, cost |
| Communication module | Send and receive JSON messages | TCP socket data | Decoded message dictionaries |
| DAO layer | Persist routers, topology, tables and logs | Model objects | JSON files |
| CLI views | Display information and request commands | User input | Terminal output |

## Architecture Diagram

```text
+----------------------------------------------------+
|                    Controller                      |
|----------------------------------------------------|
| Router Registry Controller                         |
| Topology Controller                                |
| Routing Controller                                 |
| Communication Controller                           |
|----------------------------------------------------|
| Router DAO | Topology DAO | Routing Table DAO      |
|----------------------------------------------------|
| Dijkstra Service | Routing Table Service           |
|----------------------------------------------------|
| TCP Server + JSON Messages                         |
+-------------------------+--------------------------+
                          |
                          | TCP + JSON
                          |
      +-------------------+-------------------+
      |                   |                   |
+-----+-----+       +-----+-----+       +-----+-----+
| Router R1 |       | Router R2 |       | Router R3 |
|-----------|       |-----------|       |-----------|
| Register  |       | Register  |       | Register  |
| Neighbors |       | Neighbors |       | Neighbors |
| Table DAO |       | Table DAO |       | Table DAO |
| CLI       |       | CLI       |       | CLI       |
+-----------+       +-----------+       +-----------+
```

## Data Plane and Control Plane

- The **control plane** is represented by the controller. It receives topology information and decides the best routes.
- The **data plane** is represented by the router applications. Each router uses its local routing table to select the next hop.

## Forwarding Table

Each routing table entry has:

| Field | Description |
|---|---|
| destination | Router destination ID |
| next_hop | Neighbor router to send traffic to |
| cost | Total path cost |

## Persistence

The project uses JSON files instead of a database to simplify deployment:

- `routers.json`
- `topology.json`
- `routing_tables.json`
- `logs.json`
