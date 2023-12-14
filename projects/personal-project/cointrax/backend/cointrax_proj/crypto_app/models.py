from django.db import models


class Crypto(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    circulating_supply = models.DecimalField(max_digits=20, decimal_places=2)
    symbol = models.CharField(max_length=200, unique=True, blank=False, null=False)

    def __str__(self):
        return f"{self.symbol} - {self.price}"
