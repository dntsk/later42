import os
import pybrake
from celery import shared_task
from pybrake.middleware.celery import patch_celery
from later42.models.urls import URL
from later42.models.article import Article
from later42.libs.content import get_content

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
def get_url_content_task(id):
    url = URL.objects.get(id=id)
    article = Article.objects.create(url=url)
    content = get_content(url.url)['rich_content']
    article.content = content
    article.save()
