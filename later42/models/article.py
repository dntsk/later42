from django.contrib.auth.models import User
from django.db import models
from later42.models.urls import URL


class Article(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    url = models.ForeignKey(URL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
