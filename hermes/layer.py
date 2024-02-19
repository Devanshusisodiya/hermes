import asyncio
import random
from hermes.storage import Storage
from hermes.agent import Agent

class Layer:
    def __init__(self, storage: Storage) -> None:
        self.pending = {}
        self.storage = storage

    async def _transact_storage(self, agent: Agent) -> bool:
        res = await self.storage.add_agent(agent=agent)
        return res
    
    def register(self, agent: Agent):
        """
        function to register an agent in the storage
        """
        result = asyncio.run(self._transact_storage(agent=agent))
        if result:
            print(f"agent {agent.name} registered!")
        else:
            print("agent already registered")

    async def _send_async(self, agent: Agent, message: str) -> bool:
        """
        coroutine to send message to an agent registered on the net
        """
        agent_reference = self.storage.agent_reference(agent)
        print(f"message : {message} sent")

        # this sleep here represents actual network latency when a message will be sent
        await asyncio.sleep(random.randint(1, 6))

        resp = await agent_reference.listen(message)
        if resp:
            await self.storage.update_directory(agent, message)

        return resp
    
    async def _send_batch(self) -> None:
        """
        couroutine to send messages to an agent in batch concurrently
        """
        routines = [self._send_async(agent, message) for agent, message in self.pending.items()]
        l = await asyncio.gather(
            *routines
        )

    def send(self, recipient: Agent, message: str) -> None:
        """
        function to send the message
        """
        self.pending[recipient] = message
        asyncio.run(self._send_batch())