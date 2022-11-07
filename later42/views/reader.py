from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.conf import settings
from later42.libs.content import get_content, sanitize_img_size
from later42.models.article import Article
from later42.models.urls import URL
from later42.tasks import get_url_content_task


@login_required
def get(request, url_id=None):
    url = URL.objects.get(
        user=request.user, id=url_id)

    content = {}

    try:
        article = Article.objects.get(url=url)
        content['rich_content'] = article.content
        content['title'] = url.title
        content['url'] = url.url
        content['rich_content'] = sanitize_img_size(content['rich_content'])
    except:
        content = get_content(url.url)
        get_url_content_task.delay(url.id)
    context = {'url': url, 'content': content}
    return render(request, 'reader.html', context)
