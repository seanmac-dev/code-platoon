# Generated by Django 3.2.12 on 2023-12-15 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_app', '0002_auto_20231215_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
