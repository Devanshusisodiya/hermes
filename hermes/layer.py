class Layer:
    def __init__(self) -> None:
        self.directory = {}

    def register(self, id: int) -> None:
        self.directory[id] = "agent_" + id