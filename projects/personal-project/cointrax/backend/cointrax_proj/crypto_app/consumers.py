import json
from channels.generic.websocket import AsyncWebsocketConsumer


class CryptoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get("action")

        if action == "SubAdd":
            # Handle subscription logic here
            await self.subscribe(data["subs"])
        elif action == "SubRemove":
            # Handle unsubscription logic here
            await self.unsubscribe(data["subs"])

    async def subscribe(self, subscriptions):
        # Implement subscription logic based on your requirements
        # You can store subscribers in a group and send updates
        # to all connected clients in that group
        pass

    async def unsubscribe(self, subscriptions):
        # Implement unsubscription logic based on your requirements
        pass
