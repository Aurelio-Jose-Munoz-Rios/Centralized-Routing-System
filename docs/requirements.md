# Requirements Document

## Product Vision

Develop a software-based centralized routing system where router applications communicate with a controller application. The controller receives topology information, computes routes, generates routing tables, and distributes them to routers.

## Product Goal

Implement a Python system composed of a controller and multiple router applications. The controller computes routing tables from the network topology and sends them to router applications using TCP and JSON messages.

## Functional Requirements

| ID | Requirement | Description | Priority |
|---|---|---|---|
| FR-01 | Router registration | Routers must register with the controller by sending router ID, IP address, and port. | High |
| FR-02 | Neighbor information exchange | Routers must send neighbor and link cost information to the controller. | High |
| FR-03 | Topology storage | The controller must store the network topology. | High |
| FR-04 | Route computation | The controller must compute shortest paths using Dijkstra algorithm. | High |
| FR-05 | Routing table generation | The controller must generate a routing table for each router. | High |
| FR-06 | Routing table delivery | The controller must send the corresponding routing table to each router. | High |
| FR-07 | Routing table visualization | Routers must display their routing tables through the command line. | Medium |
| FR-08 | Link cost update | The system should allow link cost updates and route recalculation. | Medium |
| FR-09 | Event logging | The system should log registrations, topology updates, calculations and routing table delivery. | Low |

## Non-Functional Requirements

| ID | Requirement | Description | Priority |
|---|---|---|---|
| NFR-01 | Python implementation | The system must be implemented in Python. | High |
| NFR-02 | Modular design | Code must be organized into clear modules using MVC + DAO. | High |
| NFR-03 | JSON messages | The system must use JSON for message exchange. | High |
| NFR-04 | Command-line interface | The system must be operated from the terminal. | High |
| NFR-05 | Error handling | The system must handle invalid messages without crashing. | Medium |
| NFR-06 | Scalability | The system should support at least four routers. | Medium |
| NFR-07 | Maintainability | The code should be readable and documented. | Medium |
| NFR-08 | Testability | The system should include documented test cases. | Medium |

## Product Backlog

| ID | Requirement | Task | Responsible | Sprint |
|---|---|---|---|---|
| PB-01 | FR-01 | Implement router registration message | Aurelio | Sprint 1 |
| PB-02 | FR-01 | Implement controller router registry | Victor | Sprint 1 |
| PB-03 | FR-02 | Define JSON format for neighbor information | Aurelio | Sprint 1 |
| PB-04 | FR-03 | Implement topology data structure | Victor | Sprint 1 |
| PB-05 | FR-04 | Implement Dijkstra algorithm | Aurelio | Sprint 2 |
| PB-06 | FR-05 | Generate routing table for each router | Aurelio | Sprint 2 |
| PB-07 | FR-06 | Send routing table from controller to router | Aurelio | Sprint 2 |
| PB-08 | FR-07 | Display routing table in router CLI | Victor | Sprint 2 |
| PB-09 | FR-08 | Simulate link cost change | Victor | Sprint 3 |
| PB-10 | FR-09 | Add event logging | Victor | Sprint 3 |

## Definition of Done

- Functionality is implemented in Python.
- Code was tested successfully.
- Expected input and output were documented.
- Acceptance criteria were met.
- Code was integrated with the rest of the system.
- Functionality can be demonstrated from the terminal.
