"""
WSGI config for immfly project.

It exposes the WSGI callable as a module-level variable named ``immfly_application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

immfly_application = get_wsgi_application()
