from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.authtoken.models import Token


class ApiKeyTests(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser1'
        self.email = 'testuser1@email.com'
        self.password = 'password1234567QWERTY'
        self.user = User.objects.create(
            username=self.username,
            email=self.email
        )
        self.user.set_password(self.password)
        self.user.save()

        self.c = Client()
        self.c.login(username=self.username, password=self.password)
        self.assertTrue(self.user.is_authenticated)
        self.response = self.c.get(reverse('api_token'))

    def test_api_key_creation(self):
        assert self.response.status_code == 302
        assert self.response.url == '/profile/'

    def test_api_key_created(self):
        token = Token.objects.get(user=self.user)
        assert token is not None

    def test_api_key_reset(self):
        token_old = Token.objects.get(user=self.user)
        self.response = self.c.get(reverse('api_token'))
        token_new = Token.objects.get(user=self.user)
        assert token_old != token_new
