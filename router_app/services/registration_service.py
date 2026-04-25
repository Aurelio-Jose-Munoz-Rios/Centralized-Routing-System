class RegistrationService:
    def __init__(self, message_service, controller_connection):
        self.message_service = message_service
        self.controller_connection = controller_connection

    def register(self, router):
        message = self.message_service.build_registration_message(router)
        return self.controller_connection.send(message)
