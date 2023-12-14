import json
from channels.generic.websocket import AsyncWebsocketConsumer
import websockets
from .models import Crypto


class CryptoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # if self.scope["user"].is_anonymous:
        #     # Reject the connection for anonymous users
        #     await self.close()
        # else:
        #     await self.accept()
        #     await self.fetch_and_broadcast_data()
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass

    async def send_crypto_data(self, event):
        await self.send(text_data=json.dumps(event))

    async def save_data_to_database(self, data):
        # Save data to the Crypto model
        await Crypto.objects.create(
            name=data.get("DISPLAY", {}).get("NAME", {}).get("FROMSYMBOL", ""),
            price=data.get("RAW", {}).get("PRICE", 0),
            circulating_supply=data.get("RAW", {}).get("SUPPLY", 0),
            symbol=data.get("RAW", {}).get("FROMSYMBOL", ""),
        )

    async def fetch_and_broadcast_data(self):
        api_key = "f0d2cf94dabf53bd48216f55644d65faca39a1b185075927bb5946ffeed27bed"
        async with websockets.connect(
            f"wss://streamer.cryptocompare.com/v2?api_key={api_key}"
        ) as websocket:
            subscribe_message = {
                "action": "SubAdd",
                "subs": [
                    "5~CCCAGG~BTC~USD",
                    "0~Coinbase~ETH~USD",
                    "2~Binance~BTC~USDT",
                ],
            }
            await websocket.send(json.dumps(subscribe_message))

            while True:
                message = await websocket.recv()
                data = json.loads(message)

                # Save data to the Crypto model
                await self.save_data_to_database(data)

                # Broadcast the data to clients
                await self.send_crypto_data({"type": "crypto_data", "data": data})
