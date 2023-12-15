from django.db import models


class Crypto(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    daily_volume = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True
    )
    market_cap = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True
    )
    # symbol = models.CharField(max_length=200, unique=True, blank=False, null=False)

    def __str__(self):
        return f"{self.name} - {self.price}"
