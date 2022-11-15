from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from later42.models.urls import URL


class ApiTests(TestCase):
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

        self.url = 'https://google.com'

        self.c = Client()
        self.c.login(username=self.username, password=self.password)
        self.assertTrue(self.user.is_authenticated)
        self.token = Token.objects.create(user=self.user)

    def test_url_create(self):
        token = Token.objects.get(user=self.user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.post(reverse('urls') + f'?url={self.url}')
        assert response.status_code == 200
        self.assertContains(response, 'success')
