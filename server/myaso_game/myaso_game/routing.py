from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/myaso_game/', consumers.GameConsumer.as_asgi()),
]