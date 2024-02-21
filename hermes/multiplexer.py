import asyncio
from asyncio import AbstractEventLoop
import random
from hermes.agent import Agent

class MultiPlexer:
    """
    Transaction Layer

    This class implements the Transaction layer in Hermes.
    It contains methods to communicate to both the Storage Layer and the Agents.
    """

    def __init__(self) -> None:
        self.agents = {}
        self.queue = asyncio.Queue()
    
    async def register(self, agent: Agent) -> bool:
        """
        Function to register an agent

            Parameters:
                    agent (Agent): An agent object
            Returns:
                    registered (bool): A boolean to represent successful registration
        """
        _registered = False

        if agent.name in self.agents:
            print("Agent already registered on the layer!!!")
        else:
            self.agents[agent.name] = agent
            _registered = True

        return _registered

    async def schedule(self, agent_name: str, message: str) -> None:
        """
        Sends the specified message to the recipent agent

            Parameters:
                    recipient (str): Name of the agent
                    message (str): Message to be sent

            Returns:
                    None
        """
        await self.queue.put(
            {
                "receiver": agent_name,
                "message": message
            }
        )

    async def send(self):
        queue_ob = await self.queue.get()
        message = queue_ob["message"]
        recv_agent = self.agents[queue_ob["receiver"]]
        await recv_agent.write(message)
    
    async def run(self):
        while True:
            await self.send()
