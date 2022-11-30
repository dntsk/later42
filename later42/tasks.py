import os

import pybrake
from celery import shared_task
from django.contrib.auth.models import User
from pybrake.middleware.celery import patch_celery

from later42.libs.content import get_content
from later42.models.article import Article
from later42.models.urls import URL

AIRBRAKE_PROJECT_ID = os.getenv('AIRBRAKE_PROJECT_ID', None)
AIRBRAKE_PROJECT_KEY = os.getenv('AIRBRAKE_PROJECT_KEY', None)

if AIRBRAKE_PROJECT_ID is not None and AIRBRAKE_PROJECT_KEY is not None:
    notifier = pybrake.Notifier(
        project_id=AIRBRAKE_PROJECT_ID,
        project_key=AIRBRAKE_PROJECT_KEY,
        environment="celery"
    )
    patch_celery(notifier)


@shared_task()
def get_url_content_task(url, user_id):
    user = User.objects.get(pk=int(user_id))
    url_object = URL(url=url, user=user)
    url_object.save()

    data = get_content(url)

    article = Article.objects.create(url=url_object)
    article.content = data.article_html
    article.title = data.title
    article.short = data.text[:150]
    if data.has_top_image():
        article.img = data.top_image

    article.save()
