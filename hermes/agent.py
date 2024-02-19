class Agent:
    """
    Agent

    This class implements the Agents in Hermes.
    It contains methods for an Agent to communicate with other Agents.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.messages = []
    
    def talk(self, layer, agent_name: str, message: str):
        """
        function to send a message
        """
        layer.send(agent_name, message)

    def notify(self) -> None:
        print("a message is received!")

    async def listen(self, message: str) -> bool:
        """
        Function to listen for messages

            Parameters:
                    message (str): The message
            Returns:
                    bool: A boolean to represent if a valid message was received
        """
        if message:
            self.notify()
            self.messages.append(message)
            return True
        else:
            return False