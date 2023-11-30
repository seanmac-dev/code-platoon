# move_app/urls.py
from django.urls import path
from .views import All_moves

urlpatterns = [path("", All_moves.as_view(), name="all_moves")]
