from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.authtoken.models import Token


@login_required
def get(request):
    token = Token.objects.filter(user=request.user)
    user = User.objects.get(username=request.user)

    if token:
        context = {"token": token[0], "user": user}
    else:
        context = {"token": None, "user": user}

    return render(request, "profile.html", context)
