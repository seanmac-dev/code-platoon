from django.shortcuts import render

# Create your views here.
from .models import Move
from .serializers import MoveSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create a view that utilizes APIView to inherit DRF's built in functionality
class All_moves(APIView):
    # establish a get method that will be triggered by GET requests
    def get(self, request):
        # utilize your ModelSerializer to serialize your queryset and return a proper response with DRF's Response
        moves = MoveSerializer(Move.objects.all(), many=True)
        # select * from move_app_move;
        return Response(moves.data)
