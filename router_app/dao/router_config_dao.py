from router_app.model.router import Router
from router_app.utils.config_loader import load_router_config


class RouterConfigDAO:
    def __init__(self, config_path):
        self.config_path = config_path

    def load_router(self):
        data = load_router_config(self.config_path)
        return Router.from_dict(data)
