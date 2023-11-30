# pokemon_app/urls.py
# import register converter to create new param types in URL patterns
from django.urls import path, register_converter

# Explicit imports
from .views import All_pokemon, A_pokemon

# import our converter class to utilize as a parameter type
from .converters import IntOrStrConverter

# To use this custom converter in a URL pattern, you need to register it with Django using the register_converter function.
register_converter(IntOrStrConverter, "int_or_str")
# Remember all urls are prefaced by http://localhost:8000/api/v1/pokemon/
urlpatterns = [
    # Currently only takes GET requests
    path("", All_pokemon.as_view(), name="all_pokemon"),
    # now we can utilize our converter for the variable we provided
    path("<int_or_str:id>/", A_pokemon.as_view(), name="a_pokemon"),
]
