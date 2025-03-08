import os
from ably import AblyRealtime
import asyncio
from fastapi import HTTPException

ABLY_API_KEY = os.getenv("ABLY_API_KEY")


# Ably Publisher
async def publish_update(event: str, data: dict):
    try:
        # Initialize Ably Realtime client
        client = AblyRealtime(ABLY_API_KEY)
        channel = client.channels.get("ticket-updates")

        # Publish a message to the channel
        await channel.publish(event, data)
        print("Message published to the channel.")

        # Close the client connection
        await client.close()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while publishing update: {str(e)}",
        )


# Ably Subscriber
class AblySubscriber:
    def __init__(self, api_key, channel_name):
        self.client = AblyRealtime(api_key)
        self.channel = self.client.channels.get(channel_name)

    async def subscribe(self):
        async def message_listener(message):
            print(f"Received message: {message.data}")

        await self.channel.subscribe(message_listener)


# Run the subscriber
async def run_subscriber():
    subscriber = AblySubscriber(ABLY_API_KEY, "ticket-updates")
    await subscriber.subscribe()

    # Keep the event loop running
    while True:
        await asyncio.sleep(1)
