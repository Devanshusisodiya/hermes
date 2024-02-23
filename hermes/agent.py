import asyncio
import random
import hashlib
from hermes.agent_base import AgentBase
from hermes.multiplexer import MultiPlexer

class Agent(AgentBase):
    """
    Agent

    This class implements the Agents in Hermes.
    It contains methods for an Agent to communicate with other Agents.
    """

    def __init__(self, name: str) -> None:
        self._hash = hashlib.sha256(bytes(name, "utf-8")).hexdigest()
        self._messages = []
        self._active = True
    
    async def talk(self, multiplexer: MultiPlexer) -> None:
        """
        Function to talk to other agents

            Parameters:
                    multiplexer (Multiplexer): The multiplexer instance
            Returns:
                    None
        """
        if self._active:
            _message = random.randint(1, 100)
            await multiplexer.schedule(self._hash, _message)
            print(f"[sndr][{self._hash}]: {_message}")

    async def write(self, message: str):
        self._messages.append(message)

    async def _get_message(self) -> str:
        """
        Function to check if messages is populated and returns it

            Parameters:
                    None
            Returns:
                    str: Message that is sent to the agent
        """
        while not len(self._messages):
            await asyncio.sleep(0.5)
        return self._messages.pop(0)

    async def _listen(self):
        """
        Function to listen for messages

            Parameters:
                    message (str): The message
            Returns:
                    bool: A boolean to represent if a valid message was received
        """
        while self._active:
            res = await self._get_message()
            if res:
                print(f"[recv][{self._hash}]: {res}")

    async def _start(self, multiplexer):
        await asyncio.gather(
            self._listen(),
            self.talk(multiplexer)
        )

    async def run(self, multiplexer):
        """
        Function to talk to other agents

            Parameters:
                    multiplexer (Multiplexer): The multiplexer instance
            Returns:
                    None
        """
        await self._start(multiplexer)