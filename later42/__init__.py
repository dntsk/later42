"""Later42 is a Django app that allows you to schedule tasks for later execution."""
from .celery import app as celery_app

__all__ = ("celery_app",)
