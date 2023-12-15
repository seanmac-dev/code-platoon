import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import websockets
from cointrax_proj.settings import env
from crypto_app.models import Crypto


class CryptoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # Start a background task to connect to Cryptocompare and fetch data
        await self.start_data_stream()

    async def disconnect(self, close_code):
        # Cleanup when the WebSocket connection is closed
        await self.stop_data_stream()

    async def receive(self, text_data):
        pass

    async def send_crypto_data(self, event):
        await self.send(text_data=json.dumps(event))

    @sync_to_async
    def save_data_to_database(self, data):
        # Save data to the Crypto model

        name = data.get("FROMSYMBOL", "")
        price = data.get("PRICE", 0.00)
        daily_volume = data.get("VOLUME24HOUR", 0.00)
        market_cap = data.get("CURRENTSUPPLYMKTCAP", 0.00)

        crypto_object, created = Crypto.objects.get_or_create(
            name=name,
            defaults={
                "price": price,
                "daily_volume": daily_volume,
                "market_cap": market_cap,
            },
        )

        if not created:
            crypto_object.price = price
            crypto_object.daily_volume = daily_volume
            crypto_object.market_cap = market_cap
            crypto_object.save()

    async def start_data_stream(self):
        api_key = env.get("API_KEY")
        async with websockets.connect(
            f"wss://streamer.cryptocompare.com/v2?api_key={api_key}"
        ) as websocket:
            subscribe_message = {
                "action": "SubAdd",
                "subs": ["5~CCCAGG~BTC~USD", "5~CCCAGG~ETH~USD", "5~CCCAGG~XRP~USD"],
            }
            await websocket.send(json.dumps(subscribe_message))

            while True:
                message = await websocket.recv()
                data = json.loads(message)

                # Save data to the Crypto model
                await self.save_data_to_database(data)

                # Broadcast the data to clients
                await self.send_crypto_data({"type": "crypto_data", "data": data})
