import asyncio
import random
from hermes.storage import Storage
from hermes.agent import Agent

class Layer:
    """
    Transaction Layer

    This class implements the Transaction layer in Hermes.
    It contains methods to communicate to both the Storage Layer and the Agents.
    """

    def __init__(self, storage: Storage) -> None:
        self.pending = {}
        self.storage = storage

    async def _transact_storage(self, agent: Agent) -> bool:
        """
        Function to register an agent

            Parameters:
                    agent (Agent): An agent object
            Returns:
                    storage_response (bool): A boolean to represent registration response from storage
        """
        storage_response = await self.storage.add_agent(agent=agent)
        return storage_response
    
    def register(self, agent: Agent):
        """
        Function to register an agent

            Parameters:
                    agent (Agent): An agent object
            Returns:
                    registered (bool): A boolean to represent successful registration
        """
        registered = asyncio.run(self._transact_storage(agent=agent))
        if registered:
            print(f"agent {agent.name} registered!")
        else:
            print("agent already registered")

    async def _send_async(self, agent_name: str, message: str) -> bool:
        """
        Coroutine to send a message to an agent

            Parameters:
                    agent_name (Agent): Name of the agent to send the message to
                    message (str): Message to be sent
            Returns:
                    agent_responded (bool): Boolean to represent whether the agent responded
        """
        agent_reference = self.storage.agent_reference(agent_name)
        print(f"message : {message} sent")

        # this sleep here represents actual network latency when a message will be sent
        await asyncio.sleep(random.randint(1, 6))

        agent_responded = await agent_reference.listen(message)
        if agent_responded:
            await self.storage.update_directory(agent_name, message)

        return agent_responded
    
    async def _send_batch(self) -> None:
        """
        Coroutine to send messages to agents concurrently

            Parameters:
                    None
            Returns:
                    None
        """
        routines = [self._send_async(agent, message) for agent, message in self.pending.items()]
        l = await asyncio.gather(
            *routines
        )

    def send(self, recipient: str, message: str) -> None:
        """
        Sends the specified message to the recipent agent

            Parameters:
                    recipient (str): Name of the agent
                    message (str): Message to be sent

            Returns:
                    None
        """
        self.pending[recipient] = message
        asyncio.run(self._send_batch())