from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from later42.models.urls import URL


class IndexTests(TestCase):
    def setUp(self) -> None:
        self.username = "testuser1"
        self.email = "testuser1@email.com"
        self.password = "password1234567QWERTY"
        self.user = User.objects.create(username=self.username, email=self.email)
        self.user.set_password(self.password)
        self.user.save()

        self.c = Client()
        self.c.login(username=self.username, password=self.password)
        self.assertTrue(self.user.is_authenticated)

    def test_url_delete(self):
        url = URL.objects.create(url="https://www.google.com/", user=self.user)
        url.save()
        self.c.delete(reverse("delete", kwargs={"url_id": url.id}))
        url = URL.objects.filter(id=url.id)
        assert len(url) == 0
