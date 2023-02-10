from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token


@login_required
def create(request):
    token = Token.objects.filter(user=request.user)
    if len(token) > 0:
        token.delete()
    token = Token.objects.create(user=request.user)
    token.save()
    return redirect("profile")
