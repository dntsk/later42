import django
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from later42.tokens import account_activation_token
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from later42.forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str


def activate(request, uidb64, token):
    try:
        uid = django.utils.encoding.force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return HttpResponse('Activation link is invalid!')
