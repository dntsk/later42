"""Forms for later42 app."""
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """Sign up form."""

    def __init__(self, *args, **kwargs):
        """Init method."""
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})
        self.fields["username"].label = "Логин"

    class Meta:
        """Meta."""

        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class CustomLoginForm(AuthenticationForm):
    """Custom login form."""

    def __init__(self, *args, **kwargs):
        """Init method."""
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["password"].widget.attrs.update({"class": "form-control"})
        self.fields["username"].label = "Логин"
