import asyncio
from hermes.agent_base import AgentBase

class MultiPlexer:
    """
    Multiplexer Layer

    This class implements the Multiplexer layer in Hermes.
    It contains methods to communicate to both the Agents.
    """

    def __init__(self) -> None:
        self._agents = {}
        self._queue = asyncio.Queue()
    
    async def register(self, agent: AgentBase) -> bool:
        """
        Function to register an agent

            Parameters:
                    agent (Agent): An agent object
            Returns:
                    registered (bool): A boolean to represent successful registration
        """
        _registered = False

        if agent._hash in self._agents:
            print(f"\nAgent already registered on the layer!!!\nHash: {agent._hash}\n")
        else:
            self._agents[agent._hash] = agent
            _registered = True

        return _registered

    async def schedule(self, agent_hash: str, message: str) -> None:
        """
        Sends the specified message to the recipent agent

            Parameters:
                    agent_hash (str): Hash of the agent
                    message (str): Message to be sent

            Returns:
                    None
        """
        await self._queue.put(
            {
                "sender": agent_hash,
                "message": message
            }
        )

    async def _send(self):
        while True:
            message = await self._queue.get()
            sender_hash = message["sender"]

            # send message to every agent but itself
            for agent_hash in self._agents:
                agent = self._agents[agent_hash]
                if agent_hash != sender_hash:
                    await agent.write(message)
    
    async def _gather_runners(self):
        _runners = [agent.run(self) for agent in self._agents.values()] + [self._send()]
        await asyncio.gather(
            *_runners
        )
    
    async def run(self):
        await self._gather_runners()
        return