"""Test signup view."""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignUpPageTests(TestCase):
    """Test signup view."""

    def setUp(self) -> None:
        """Set up test data."""
        self.username = "testuser"
        self.email = "testuser@email.com"
        self.password = "password1234567QWERTY"

    def test_signup_page_url(self):
        """Test the signup page url."""
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="registration/signup.html")

    def test_signup_page_view_name(self):
        """Test the signup page view name."""
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="registration/signup.html")

    def test_signup_form(self):
        """Test the signup form."""
        response = self.client.post(
            reverse("signup"),
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password,
                "password2": self.password,
            },
        )
        self.assertEqual(response.status_code, 200)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)
