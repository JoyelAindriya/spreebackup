"""
ASGI config for inter project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from routing import websocket_urlpatterns  # Import your WebSocket URL patterns
from consumers import ChatConsumer  # Import your WebSocket consumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inter.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),  # For HTTP requests
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # Add your WebSocket URL patterns here
        )
    ),
})
