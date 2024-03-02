import asyncio
import random
import typing as T

from hermes.agent_base import AgentBase
from hermes.multiplexer import MultiPlexer


class Agent(AgentBase):
    """
    Agent

    This class implements the Agents in Hermes.
    It contains methods for an Agent to communicate with other Agents.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)

    async def talk(self, multiplexer: MultiPlexer) -> None:
        """
        Function to talk to other agents

        Parameters:
                multiplexer (Multiplexer): The multiplexer instance
        Returns:
                None
        """
        if self.active:
            _message = str(random.randint(1, 100))
            await multiplexer.schedule(self.hash, _message)
            print(f"[sndr][{self.hash}]: {_message}")

    async def write(self, message: T.Dict[str, str]):
        self.messages.append(message)

    async def _get_message(self) -> T.Dict[str, str]:
        """
        Function to check if messages is populated and returns it

        Parameters:
                None
        Returns:
                str: Message that is sent to the agent
        """
        while not len(self.messages):
            await asyncio.sleep(0.5)
        return self.messages.pop(0)

    async def _listen(self):
        """
        Function to listen for messages

        Parameters:
            message (str): The message
        Returns:
            bool: A boolean to represent if a valid message was received
        """
        while self.active:
            res = await self._get_message()
            if res:
                print(f"[recv][{self.hash}]: {res}")

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
