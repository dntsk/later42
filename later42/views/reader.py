from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from later42.libs.content import get_content, sanitize_img_size
from later42.models.article import Article
from later42.models.urls import URL


@login_required
def get(request, url_id=None):
    url = URL.objects.get(
        user=request.user, id=url_id)
    content = {}
    try:
        article = Article.objects.get(url=url)
        content['title'] = article.title
        content['url'] = url.url
        content['rich_content'] = sanitize_img_size(article.content)
    except:
        content = get_content(url.url)
        content['rich_content'] = sanitize_img_size(content.article_html)
    context = {'url': url, 'content': content}
    return render(request, 'reader.html', context)
