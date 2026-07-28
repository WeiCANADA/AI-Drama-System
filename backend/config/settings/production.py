from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F403


DEBUG = env_bool("DJANGO_DEBUG", False)  # noqa: F405

if not env("DJANGO_SECRET_KEY"):  # noqa: F405
    raise ImproperlyConfigured("DJANGO_SECRET_KEY must be set for production settings.")
