from django.shortcuts import get_object_or_404
from .models import Crypto  # imports the Pokemon model
from .serializers import CryptoSerializer  # imports the PokemonSerializer

# from django.http import (
#     JsonResponse,
# )  # Our responses will now be returned in JSON so we should utilize a JsonResponse

# Import both APIView and Response from DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
)

# Create your views here.

# def all_pokemon(request):
#     pokemon = PokemonSerializer(Pokemon.objects.order_by('name'), many=True) # Utilize the serializer to serialize all of our Pokemon pulled from the Database
#     return JsonResponse({"pokemon": pokemon.data}) # JSON could only be interpreted in dictionary format so we need to ensure our response is a dictionary itself.


class All_crypto(APIView):
    # Just like we said before we only want this information available for GET requests therefore we have to place this logic under a GET method. DRF will recognize the `get` method and trigger that method every time a GET request is sent
    def get(self, request):
        crypto = CryptoSerializer(Crypto.objects.all(), many=True)
        # Under response we don't necessarily need to send information in JSON format instead DRF will format our response and make it acceptable for Front-End frameworks
        return Response(crypto.data)
