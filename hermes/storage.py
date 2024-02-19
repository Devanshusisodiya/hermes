import os
import pickle as pkl
from typing import Dict
from hermes.agent import Agent

class Storage:
    """
    Storage

    This class implements the Storage layer in Hermes.
    It contains methods that allow manipulation of the agent directory.
    """
    
    def __init__(self) -> None:
        # uncomment to maintain a persistent agent storage
        # if "agents.pkl" not in os.listdir(os.getcwd()):
        self.agents_path = os.getcwd() + "/agents.pkl"
        with open(self.agents_path, "wb") as f:
            directory = {}
            pkl.dump(directory, f)

    async def add_agent(self, agent: Agent) -> bool:
        """
        Returns the whether an agent exists after adding it to the network

            Parameters:
                    agent (Agent): An agent instance

            Returns:
                    agent_exists (bool): A boolean
        """
        with open(self.agents_path, "rb") as f:
            directory = pkl.load(f)

        agent_exists = False # to keep track whether the agent exists
    
        # update the directory
        if agent.name not in directory:
            directory[agent.name] = agent
            agent_exists = True
        else:
            print(f"Agent {agent.name} already exists on the network!!!")
            
        with open(self.agents_path, "wb") as f:
            pkl.dump(directory, f)

        return agent_exists
    
    async def update_directory(self, agent_name: str, message: str) -> None:
        """
        Updates the agent directory for the agent specified with the message

            Parameters:
                    agent (Agent): An agent instance
                    message (str): A message string

            Returns:
                    None
        """
        with open(self.agents_path, "rb") as f:
            directory = pkl.load(f)
        
        # updating the agent messages
        directory[agent_name].messages.append(message)

        with open(self.agents_path, "wb") as f:
            pkl.dump(directory, f)

    def agent_reference(self, agent_name: str) -> Agent:
        """
        Returns the storage reference of the agent object from the agent directory

            Parameters:
                    agent_name (str): Name of the agent

            Returns:
                    agent (Agent): Agent object
        """
        with open(self.agents_path, "rb") as f:
            directory = pkl.load(f)

        agent = directory[agent_name]
        return agent