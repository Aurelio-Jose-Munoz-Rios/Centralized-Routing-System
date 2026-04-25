# API Messages

All messages are JSON objects encoded as UTF-8 and sent through TCP. Each message is terminated by a newline character.

## REGISTER_ROUTER

Sent by a router to register with the controller.

```json
{
  "type": "REGISTER_ROUTER",
  "router_id": "R1",
  "ip": "127.0.0.1",
  "port": 5001
}
```

## TOPOLOGY_UPDATE

Sent by a router to inform its neighbors and link costs.

```json
{
  "type": "TOPOLOGY_UPDATE",
  "router_id": "R1",
  "neighbors": [
    {"neighbor_id": "R2", "cost": 2},
    {"neighbor_id": "R3", "cost": 5}
  ]
}
```

## GET_ROUTING_TABLE

Sent by a router when it needs its current table.

```json
{
  "type": "GET_ROUTING_TABLE",
  "router_id": "R1"
}
```

## LINK_COST_UPDATE

Sent by a router or administrator to update a link cost.

```json
{
  "type": "LINK_COST_UPDATE",
  "router_id": "R1",
  "source_router": "R1",
  "destination_router": "R3",
  "cost": 1
}
```

## ACK

```json
{
  "type": "ACK",
  "message": "Operation completed successfully."
}
```

## ERROR

```json
{
  "type": "ERROR",
  "message": "Invalid message format."
}
```

## ROUTING_TABLE Response

```json
{
  "type": "ACK",
  "message": "Routing table generated.",
  "routing_table": [
    {"destination": "R2", "next_hop": "R2", "cost": 2},
    {"destination": "R4", "next_hop": "R2", "cost": 6}
  ]
}
```
