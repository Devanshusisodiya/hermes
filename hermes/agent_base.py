from abc import abstractmethod

class AgentBase:
    """
    AgentBase class

    This is the base class to implement Agents in Hermes.
    """

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def run(self):
        pass