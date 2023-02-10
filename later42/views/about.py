"""About page view."""
from django.shortcuts import render


def get(request):
    """About page view."""
    return render(request, "about.html")
