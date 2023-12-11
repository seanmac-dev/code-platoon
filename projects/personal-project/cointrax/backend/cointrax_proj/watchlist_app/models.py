from django.db import models
from user_app.models import User
from crypto_app.models import Crypto


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    crypto = models.ManyToManyField(Crypto, related_name="watchlists")
