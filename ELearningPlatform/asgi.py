"""
ASGI config for ELearningPlatform project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter  # 1. import
from channels.auth import AuthMiddlewareStack  # 1. import
import chat.routing  # 1. import

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ELearningPlatform.settings")

django_asgi_app = get_asgi_application()  # 2. change var name before assigning application

application = ProtocolTypeRouter({  # 3. ProtocolTypeRouter config
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(chat.routing.websocket_urlpatterns)
    ),
})

# do not forget set ASGI_APPLICATION to settings
