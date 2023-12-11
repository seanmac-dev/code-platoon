# Generated by Django 4.2.4 on 2023-12-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_app', '0002_alter_crypto_circulating_supply_alter_crypto_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='circulating_supply',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
