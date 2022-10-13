from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class LoginPageTests(TestCase):
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

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        assert response.status_code == 200

    def test_index_page_after_login(self):
        response = self.c.get(reverse('index'))
        assert response.status_code == 200
        assert response.context['user'].is_authenticated
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, '/accounts/logout/')

    def test_profile_page_template(self):
        response = self.c.get(reverse('profile'))
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'profile.html')

    def test_api_key_creation_button(self):
        response = self.c.get(reverse('profile'))
        assert response.status_code == 200
        self.assertContains(response, 'id="createbutton"')
