class Agent:
    def __init__(self, name: str) -> None:
        self.name = name
        self.messages = []
    
    def comm(self, layer, agent: str, message: str):
        """
        function to send a message
        """
        layer.send(agent, message)

    async def recv(self, message: str):
        """
        function to receive a message
        """
        print(f"recieved message : {message}")
        self.messages.append(message)
        return "message received"