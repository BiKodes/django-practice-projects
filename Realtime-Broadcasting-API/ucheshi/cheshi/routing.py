from django.urls import path
from .consumers import CheshiConsumer


ws_urlpatterns = [
    path('ws/cheshi/', CheshiConsumer.as_asgi())
]