from hermes.agent import Agent
from hermes.hermes import multiplexer
import asyncio
import random


async def recv_handler(message):
    print("[recv] : {}".format(message))
    return False

async def send_handler(message):
    print("[sent] : {}".format(message))
    return False


async def main():

    a1 = Agent("a1")
    a2 = Agent("a2")

    await multiplexer.register(a1)
    await multiplexer.register(a2)

    try:
        await asyncio.gather(
            a1.run(multiplexer, a2.name, "from a1"),
            a2.run(multiplexer, a1.name, "from a2"),
            multiplexer.run()
        )
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    asyncio.run(main())