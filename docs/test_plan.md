# Requirements Test Plan

## Objective

Verify that the centralized routing system satisfies the defined functional and non-functional requirements.

## Test Environment

| Element | Description |
|---|---|
| Operating system | Windows 10, Linux or macOS |
| Python version | Python 3.10+ |
| Communication protocol | TCP |
| Data format | JSON |
| Number of routers | 4 sample routers |
| Controller IP | 127.0.0.1 |
| Controller port | 9000 |

## Functional Test Cases

| Test case | Requirement | Description | Expected result |
|---|---|---|---|
| TC-01 | FR-01 | Register router R1 | Controller stores R1 and returns ACK |
| TC-02 | FR-02, FR-03 | Send R1 neighbors | Controller stores topology links |
| TC-03 | FR-04 | Run Dijkstra | Shortest paths are computed correctly |
| TC-04 | FR-05 | Generate routing table | Table contains destination, next hop and cost |
| TC-05 | FR-06 | Send table to router | Router receives and stores table |
| TC-06 | FR-07 | Display routing table | CLI prints table entries |
| TC-07 | FR-08 | Update link cost | Controller recalculates affected routes |
| TC-08 | NFR-05 | Send invalid JSON | Controller returns ERROR and continues running |

## Execution Summary Template

| Total test cases | Passed | Failed | Pending | Success percentage |
|---|---|---|---|---|
| 8 | 0 | 0 | 8 | 0% |
