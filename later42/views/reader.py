from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.conf import settings
from later42.libs.content import get_content, sanitize_img_size
from later42.models.urls import URL


@login_required
def get(request, url_id=None):
    url = URL.objects.get(
        user=request.user, archived=False, id=url_id)
    content = get_content(url.url)
    content['rich_content'] = sanitize_img_size(content['rich_content'])
    context = {'url': url, 'content': content}
    return render(request, 'reader.html', context)