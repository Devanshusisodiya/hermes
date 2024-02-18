import os

class Storage:
    def __init__(self) -> None:
        if "agent.json" not in os.listdir(os.getcwd()):
            with open(os.getcwd() + "/agents.json", "w") as f:
                pass