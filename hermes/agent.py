class Agent:
    def __init__(self, name: str) -> None:
        self.name = name
        self.messages = []
    
    def talk(self, layer, agent: str, message: str):
        """
        function to send a message
        """
        layer.send(agent, message)

    async def listen(self, message: str) -> bool:
        """
        function to receive a message
        """
        if message:
            print(f"recieved message : {message}")
            self.messages.append(message)
            return True
        else:
            return False