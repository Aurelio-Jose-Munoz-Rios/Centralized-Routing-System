class ForwardingController:
    def __init__(self, forwarding_service, view):
        self.forwarding_service = forwarding_service
        self.view = view
