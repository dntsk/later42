from django.db import models
from later42.models.urls import URL


class Article(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    url = models.ForeignKey(URL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=2000, blank=True, null=True)
    short = models.TextField(blank=True, null=True)
    img = models.URLField(blank=True, null=True)
