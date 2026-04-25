from controller_app.model.router import Router


class RouterRegistryController:
    def __init__(self, router_dao, log_dao):
        self.router_dao = router_dao
        self.log_dao = log_dao

    def register_router(self, router_id, ip, port):
        router = Router(router_id, ip, port)
        self.router_dao.insert_or_update(router)
        self.log_dao.add("REGISTER_ROUTER", f"Router {router_id} registered from {ip}:{port}")
        return router

    def list_routers(self):
        return self.router_dao.find_all()
