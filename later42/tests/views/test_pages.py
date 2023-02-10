"""Test pages views."""
from django.test import TestCase
from django.urls import reverse


class PageTests(TestCase):
    """Test pages views."""

    def test_index_page_url(self):
        """Test index page url"""
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="index.html")

    def test_about_page_url(self):
        """Test about page url"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="about.html")

    def test_profile_page_url_redirect(self):
        """Test profile page url redirect"""
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 302)
