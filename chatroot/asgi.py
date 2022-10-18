import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chatroot import routings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatroot.settings')

application = ProtocolTypeRouter({

    "http": get_asgi_application(),
    "websocket": URLRouter(routings.websocket_urlpatterns),
})
