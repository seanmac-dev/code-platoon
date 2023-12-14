from django.urls import path
from crypto_app.consumers import CryptoConsumer

websocket_urlpatterns = [
    path("ws/crypto/", CryptoConsumer.as_asgi()),
]
