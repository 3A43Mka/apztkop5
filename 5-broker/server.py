class Server:
    def __init__(self, server_name):
        self.server_name = server_name

    def process(self, obj):
        obj['result'] = f'Result provided by {self.server_name}.'
