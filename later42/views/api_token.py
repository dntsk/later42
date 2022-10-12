from django.shortcuts import redirect
from rest_framework.authtoken.models import Token


def create(request):
    token = Token.objects.filter(user=request.user)
    try:
        token.delete()
    except:
        pass
    token = Token.objects.create(user=request.user)
    token.save()
    return redirect('profile')