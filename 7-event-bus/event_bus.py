class EventBus:
    def __init__(self):
        self.listeners = {}

    def add_event_listener(self, event, listener):
        if event not in self.listeners:
            self.listeners[event] = []
        self.listeners[event].append(listener)

    def emit(self, event, arguments=None):
        if event in self.listeners:
            for listener in self.listeners[event]:
                listener(arguments)

    def unsubscribe(self, event, listener):
        if event in self.listeners:
            if listener in self.listeners[event]:
                self.listeners[event].remove(listener)
