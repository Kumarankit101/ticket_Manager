import ably
from ably import AblyRealtime
import asyncio


class AblySubscriber:
    def __init__(self, api_key, channel_name):
        self.client = AblyRealtime(api_key)
        self.channel = self.client.channels.get(channel_name)

    async def subscribe(self):
        async def message_listener(message):
            print(f"Received message: {message.data}")

        await self.channel.subscribe(message_listener)


async def main():
    subscriber = AblySubscriber(
        "tVOuoA.3EItZQ:F6KttkjAkb-LWfaiFkT3e9pRkDkctSzWLiMLyOltDCY", "ticket-updates"
    )
    await subscriber.subscribe()

    # Keep the event loop running
    while True:
        await asyncio.sleep(1)


# Run the main function within an event loop
asyncio.run(main())
