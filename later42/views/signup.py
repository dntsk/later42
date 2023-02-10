"""Signup view."""
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from later42.forms import SignUpForm
from later42.tokens import account_activation_token


def register(request):
    """Register user."""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # raw_password = form.cleaned_data.get("password1")

            current_site = get_current_site(request)

            mail_subject = "Later42: Активация аккаунта"
            message = render_to_string(
                "registration/email_activation.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            to_email = form.cleaned_data.get("email")
            email = EmailMessage(
                mail_subject, message, to=[to_email], from_email=settings.EMAIL_FROM
            )
            email.send()

            return render(request, "registration/email_sent.html")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})
