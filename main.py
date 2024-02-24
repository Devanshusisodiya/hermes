from hermes.agent import Agent
from hermes.hermes import multiplexer
import asyncio

async def main():

    a1 = Agent("a1")
    a2 = Agent("a2")
    a3 = Agent("a3")
    a4 = Agent("a4")

    await multiplexer.register(a1)
    await multiplexer.register(a2)
    await multiplexer.register(a3)
    await multiplexer.register(a4)

    # trying to register already registered agent
    await multiplexer.register(a3)

    await asyncio.gather(
        multiplexer.run()
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nstopping multiplexer\n")