# pokemon_app/serializers.py
from rest_framework import serializers
from .models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    moves = serializers.SerializerMethodField()

    # here we tell our serializer to utilize the method creating below to and place the methods return value into the 'moves' field. We only have to create a method because this is a many-to-many relationship. All other relationships would just take the model serializer instead of SerializerMethodField.
    class Meta:
        model = Pokemon
        fields = "__all__"

    def get_moves(self, instance):
        moves = instance.moves.all()
        move_names = [move.name for move in moves]
        return move_names
