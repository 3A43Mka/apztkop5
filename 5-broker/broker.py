class Broker:
    def __init__(self, high_tier_server, med_tier_server, low_tier_server):
        self.high_tier_server = high_tier_server
        self.med_tier_server = med_tier_server
        self.low_tier_server = low_tier_server

    def process(self, obj):
        if obj['subscription'] == 'high':
            self.high_tier_server.process(obj)
        elif obj['subscription'] == 'medium':
            self.med_tier_server.process(obj)
        else:
            self.low_tier_server.process(obj)
