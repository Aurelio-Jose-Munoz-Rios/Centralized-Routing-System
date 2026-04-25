# Centralized Routing System

Proyecto académico en Python para simular un sistema de enrutamiento centralizado. El sistema está compuesto por una aplicación **Controller** y varias aplicaciones **Router** que se comunican mediante sockets TCP y mensajes JSON.

El diseño sigue una arquitectura MVC + DAO, similar al ejemplo de Router Management CLI, pero adaptada al dominio de la capa de red: registro de routers, recopilación de topología, cálculo de rutas, generación de tablas de enrutamiento y simulación de decisiones de forwarding.

## Relación con capa de red

El proyecto separa claramente dos responsabilidades:

- **Plano de control:** el Controller mantiene la vista global de la red, ejecuta Dijkstra y genera tablas de enrutamiento.
- **Plano de datos:** cada Router recibe su tabla y decide el siguiente salto para llegar a un destino.

Esta separación es similar al enfoque SDN estudiado en capa de red, donde un controlador remoto calcula e instala tablas de forwarding en los routers.

## Funcionalidades

- Registro de routers en el controlador.
- Envío de información de vecinos y costos de enlace.
- Almacenamiento de la topología como lista de adyacencia.
- Cálculo de caminos mínimos con Dijkstra.
- Generación de tablas de enrutamiento por router.
- Entrega de tablas de enrutamiento mediante JSON.
- Visualización de routers, topología y tablas desde CLI.
- Simulación de cambio de costo de enlace.
- Manejo de mensajes JSON inválidos.
- Persistencia en archivos JSON mediante DAO.
- Pruebas unitarias de los módulos principales.

## Estructura del proyecto

```text
centralized-routing-system/
├── controller_app/
│   ├── main.py
│   ├── config/
│   │   └── controller_config.json
│   ├── controller/
│   │   ├── controller_app_controller.py
│   │   ├── communication_controller.py
│   │   ├── router_registry_controller.py
│   │   ├── routing_controller.py
│   │   └── topology_controller.py
│   ├── dao/
│   │   ├── log_dao.py
│   │   ├── router_dao.py
│   │   ├── routing_table_dao.py
│   │   └── topology_dao.py
│   ├── data/
│   │   ├── logs.json
│   │   ├── routers.json
│   │   ├── routing_tables.json
│   │   └── topology.json
│   ├── model/
│   │   ├── link.py
│   │   ├── router.py
│   │   ├── routing_table.py
│   │   ├── routing_table_entry.py
│   │   └── topology.py
│   ├── network/
│   │   ├── client_handler.py
│   │   ├── tcp_server.py
│   │   └── udp_server.py
│   ├── services/
│   │   ├── dijkstra_service.py
│   │   ├── message_service.py
│   │   ├── routing_table_service.py
│   │   └── topology_service.py
│   ├── utils/
│   │   ├── config_loader.py
│   │   ├── json_utils.py
│   │   └── logger.py
│   └── views/
│       ├── controller_cli_view.py
│       ├── log_view.py
│       ├── routing_table_view.py
│       └── topology_view.py
├── router_app/
│   ├── main.py
│   ├── config/
│   │   ├── router_R1.json
│   │   ├── router_R2.json
│   │   ├── router_R3.json
│   │   └── router_R4.json
│   ├── controller/
│   ├── dao/
│   ├── data/
│   ├── model/
│   ├── network/
│   ├── services/
│   ├── utils/
│   └── views/
├── docs/
│   ├── api_messages.md
│   ├── architecture.md
│   ├── network_layer_notes.md
│   ├── requirements.md
│   ├── sequence.md
│   └── test_plan.md
├── tests/
├── tools/
│   └── demo_network.py
├── README.md
├── read.md
└── requirements.txt
```

## Requisitos

- Python 3.10 o superior.
- Terminal o consola.
- No requiere base de datos externa.

## Instalación

```bash
git clone <repository-url>
cd centralized-routing-system
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

En Linux/macOS:

```bash
source .venv/bin/activate
```

Instala dependencias opcionales para pruebas:

```bash
pip install -r requirements.txt
```

## Ejecución del controlador

Desde la raíz del proyecto:

```bash
python controller_app/main.py
```

Comandos disponibles en el Controller CLI:

```text
help
show routers
show topology
show table <router_id>
show tables
compute routes
update cost <source_router> <destination_router> <cost>
show logs
exit
```

## Ejecución de routers

Abre una terminal diferente para cada router. Ejemplos:

```bash
python router_app/main.py router_app/config/router_R1.json
python router_app/main.py router_app/config/router_R2.json
python router_app/main.py router_app/config/router_R3.json
python router_app/main.py router_app/config/router_R4.json
```

Comandos disponibles en el Router CLI:

```text
help
register
send topology
request table
show routing-table
forward <destination_router>
update cost <neighbor_router> <cost>
exit
```

## Demo rápida

1. Inicia el controlador:

```bash
python controller_app/main.py
```

2. En otra terminal ejecuta:

```bash
python tools/demo_network.py
```

El demo registra cuatro routers, envía sus vecinos, calcula las rutas y muestra las tablas generadas.

## Ejecutar pruebas

```bash
python -m unittest discover -s tests
```

## Ejemplo de mensaje JSON

```json
{
  "type": "REGISTER_ROUTER",
  "router_id": "R1",
  "ip": "127.0.0.1",
  "port": 5001
}
```

## Equipo

- Aurelio Jose Muñoz - Developer
- Victor Felipe Chavarro Cepeda - Tester, documentador

## Profesor

Oscar Mauricio Caicedo Rendon
# Centralized-Routing-System
