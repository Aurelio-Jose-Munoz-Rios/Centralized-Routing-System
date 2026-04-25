class MessageService:
    def ack(self, message, extra_data=None):
        response = {
            "type": "ACK",
            "message": message
        }
        if extra_data:
            response.update(extra_data)
        return response

    def error(self, message):
        return {
            "type": "ERROR",
            "message": message
        }

    def require_fields(self, message, fields):
        missing = [field for field in fields if field not in message]
        if missing:
            raise ValueError(f"Missing fields: {', '.join(missing)}")
