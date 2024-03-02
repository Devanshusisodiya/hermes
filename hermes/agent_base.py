import hashlib
import typing as T
from abc import abstractmethod


class AgentBase:
    """
    AgentBase class

    This is the base class to implement Agents in Hermes.
    """
    def __init__(self, name: str) -> None:
        self.hash: str = hashlib.sha256(bytes(name, "utf-8")).hexdigest()
        self.messages: T.List[T.Dict[str, str]] = []
        self.active: bool = True

    @abstractmethod
    async def write(self, message: T.Dict[str, str]):
        pass

    @abstractmethod
    async def run(self):
        pass
