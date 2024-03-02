# Hermes

This is a POC project to understand how agents in a multi agent environment can interact with each other.

Current implementation defines an _Agent Layer_ which rests on top of a _Multiplexer Layer_. The idea is pretty simple, an agent can be registered on the
multiplexer and can then send messages to all other agents on the network.

<img width="1590" alt="image" src="https://github.com/Devanshusisodiya/hermes/assets/43195822/1810843e-87e1-4c21-967a-a0a9d5c8c63a">

Under the hood, the multiplexer uses the following architecture.

<img width="1420" alt="image" src="https://github.com/Devanshusisodiya/hermes/assets/43195822/b0f72d4a-ba88-4495-90e7-9dd608a88529">

The aggregator function is invoked which puts up the messages on the multiplexer messsage bus (async. queue) when an agent makes contact, and the scheduler function which is running constantly consumes the messages
put on message bus and sends them to the agents registered on the network.

An agent can be defined and registered on the multiplexer as follows

```python
awesome_agent = Agent("awesome_agent")

await multiplexer.register(awesome_agent)
```

And finally the mutiplexer is to be run

```python
await multiplexer.run()
```

A sample driver code is defined in `main.py`. 

### This idea can be evolved

From a broader perspective, this environment can be evolved to use multiple _P2P_ hosts that use **Hermes** package (which under the hood will use sockets to make public remote connections) to run agents.
