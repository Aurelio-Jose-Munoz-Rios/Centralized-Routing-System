class LogView:
    def show(self, logs):
        for item in logs:
            print(f"{item['timestamp']} | {item['event_type']} | {item['message']}")
