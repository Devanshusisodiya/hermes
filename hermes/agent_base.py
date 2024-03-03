"""AgentBase module"""

import hashlib
import typing as T
from abc import abstractmethod


class AgentBase:
    """
    AgentBase class

    This is the base class to implement Agents in Hermes.
    """

    def __init__(self, name: str) -> None:
        """Initialize hash"""
        self.hash: str = hashlib.sha256(bytes(name, "utf-8")).hexdigest()

    @abstractmethod
    async def write(self, message: T.Dict[str, str]) -> None:
        """
        Abstract method to write to the messages
        list of the agent
        """

    @abstractmethod
    async def run(self, multiplexer) -> None:
        """
        Abstract method to run the agent
        """
