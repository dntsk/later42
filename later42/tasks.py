from celery import shared_task
from later42.models.urls import URL
from later42.models.article import Article
from later42.libs.content import get_content


@shared_task()
def get_url_content_task(id):
    url = URL.objects.get(id=id)
    article = Article.objects.create(url=url)
    content = get_content(url.url)['rich_content']
    article.content = content
    article.save()
