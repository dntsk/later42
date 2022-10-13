from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from later42.forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
