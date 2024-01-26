"""
ASGI config for the immfly project.

It exposes the ASGI callable as a module-level variable named ``immfly_application``.

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

immfly_application = get_asgi_application()
