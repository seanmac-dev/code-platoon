from rest_framework.serializers import ModelSerializer
from .models import Crypto


class CryptoSerializer(ModelSerializer):
    class Meta:
        model = Crypto
        fields = "__all__"
