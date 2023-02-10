"""Account activation view."""
import django
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from later42.tokens import account_activation_token

django.utils.encoding.force_text = force_str


def activate(request, uidb64, token):
    """Activate user account."""
    try:
        uid = django.utils.encoding.force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("index")
    else:
        return HttpResponse("Activation link is invalid!")
