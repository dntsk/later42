from django.contrib.auth.models import User
from django.db import models


class URL(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=2000)
    title = models.CharField(max_length=2000)
    archived = models.BooleanField(default=False)
