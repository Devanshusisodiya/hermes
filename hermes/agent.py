import asyncio

class Agent:
    """
    Agent

    This class implements the Agents in Hermes.
    It contains methods for an Agent to communicate with other Agents.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.messages = []
        self.active = True
    
    async def talk(self, multiplexer, agent_name: str, message: str):
        """
        function to send a message
        """
        # put a message on the event loop queue
        # then call a connective function from layer to pass the loop
        await multiplexer.schedule(agent_name, message)
        print("sent")

    async def write(self, message: str):
        self.messages.append(message)

    async def listen(self) -> str:
        """
        Function to listen for messages

            Parameters:
                    message (str): The message
            Returns:
                    bool: A boolean to represent if a valid message was received
        """
        while not len(self.messages):
            await asyncio.sleep(0.5)
        return self.messages.pop(0)
    
    async def listen_forever(self):
        while self.active:
            res = await self.listen()
            if res:
                print(f"[recv]: {res}")
    
    async def start(self, multiplexer, agent_name, message):
        await asyncio.gather(
            self.listen_forever(),
            self.talk(multiplexer, agent_name, message)
        )

    async def run(self, multiplexer, agent_name, message):
        await self.start(multiplexer, agent_name, message)