import os
import pickle as pkl
from typing import Dict
from hermes.agent import Agent

class Storage:
    def __init__(self) -> None:
        # uncomment to maintain a persistent agent storage
        # if "agents.pkl" not in os.listdir(os.getcwd()):
        self.agents_path = os.getcwd() + "/agents.pkl"
        with open(self.agents_path, "wb") as f:
            directory = {}
            pkl.dump(directory, f)

    async def add_agent(self, agent: Agent) -> bool:
        """
        function to update the agent directory
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
            # raise Exception("Agent already exists on the network!!!")
            
        with open(self.agents_path, "wb") as f:
            pkl.dump(directory, f)

        return agent_exists
    
    async def update_directory(self, agent: Agent, message: str) -> None:
        with open(self.agents_path, "rb") as f:
            directory = pkl.load(f)
        
        # updating the agent messages
        directory[agent.name].messages.append(message)

        with open(self.agents_path, "wb") as f:
            pkl.dump(directory, f)

    def agent_reference(self, agent: Agent) -> Dict:
        """
        function to access the agent directory
        """
        with open(self.agents_path, "rb") as f:
            directory = pkl.load(f)

        return directory[agent.name]