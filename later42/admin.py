"""Admin configuration for later42 app."""
from django.contrib import admin

from .models.urls import URL

admin.site.register(URL)
