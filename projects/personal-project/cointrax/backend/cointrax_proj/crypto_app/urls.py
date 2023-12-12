from django.urls import path
from .views import All_crypto

urlpatterns = [
    path("", All_crypto.as_view(), name="all_crypto"),
]
