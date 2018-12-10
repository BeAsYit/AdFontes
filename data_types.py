class Video:
    def __init__(self, index):
        self.index = index
        self.size = 0


class Endpoint:
    def __init__(self, index):
        self.index = index
        self.datacenter_latency = 0
        self.servers = []
        self.requests = []


class Server:
    def __init__(self, index):
        self.index = index
        self.capacity = 0
        self.videos = []
        self.endpoints = []
