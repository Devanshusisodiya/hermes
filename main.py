from hermes.agent import Agent
from hermes.hermes import storage, layer

a1 = Agent("a1")
a2 = Agent("a2")

layer.register(a1)
layer.register(a2)

# sending the message from agent a1 to agent a2
# the only the name is passed because an agent can be existing
# in a different namespace, and the communication can be done with name alone
a1.talk(layer, "a2", "message from a1")