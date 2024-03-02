import asyncio
import random
import typing as T

from hermes.agent_base import AgentBase


class MultiPlexer:
    """
    Multiplexer Layer

    This class implements the Multiplexer layer in Hermes.
    It contains methods to communicate to both the Agents.
    """

    def __init__(self) -> None:
        self._agents: T.Dict[str, AgentBase] = {}
        self._queue: asyncio.Queue = asyncio.Queue()

    async def register(self, agent: AgentBase) -> bool:
        """
        Function to register an agent

        Parameters:
                agent (Agent): An agent object
        Returns:
                registered (bool): A boolean to represent
                successful registration
        """
        _registered = False

        if agent.hash in self._agents:
            print(f"\nAgent already registered!\nHash: {agent.hash}\n")
        else:
            self._agents[agent.hash] = agent
            _registered = True

        return _registered

    async def schedule(self, agenthash: str, message: str) -> None:
        """
        Sends the specified message to the recipent agent

        Parameters:
                agenthash (str): Hash of the agent
                message (str): Message to be sent
        Returns:
                None
        """
        await self._queue.put({"sender": agenthash, "message": message})

    async def _send(self):
        while True:
            message = await self._queue.get()
            senderhash = message["sender"]

            # send message to every agent but itself
            for agenthash in self._agents:
                agent = self._agents[agenthash]
                if agenthash != senderhash:
                    # simulating actual different network latencies
                    # to contact agents on the network
                    await asyncio.sleep(random.randint(1, 10))
                    await agent.write(message)

    async def _gather_runners(self):
        _runners = [agent.run(self) for agent in self._agents.values()]
        await asyncio.gather(*_runners, self._send())

    async def run(self):
        await self._gather_runners()
        return
