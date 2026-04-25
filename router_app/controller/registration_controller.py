class RegistrationController:
    def __init__(self, registration_service, view, log_dao):
        self.registration_service = registration_service
        self.view = view
        self.log_dao = log_dao

    def register(self, router):
        response = self.registration_service.register(router)
        self.log_dao.add("REGISTER_ROUTER", str(response))
        self.view.show_response(response)
        return response
