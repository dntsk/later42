from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from later42.forms import SignUpForm
from later42.tokens import account_activation_token


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.refresh_from_db()
            user.is_active = False
            user.save()
            raw_password = form.cleaned_data.get('password1')

            current_site = get_current_site(request)

            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)

            mail_subject = 'Later42: Активация аккаунта'
            message = render_to_string('email_activation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()

            return render(request, 'email_sent.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
