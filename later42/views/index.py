from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.conf import settings

from later42.models.article import Article
from later42.models.urls import URL


def get(request):
    data = {}
    try:
        urls = URL.objects.filter(
            user=request.user, archived=False).order_by('-id')
        data = Article.objects.filter(url__in=urls).select_related('url')
    except:
        urls = []
    context = {'data': data}
    return render(request, 'index.html', context)


@login_required
def archive(request, url_id=None):
    if url_id:
        URL.objects.filter(id=url_id, user=request.user).update(archived=True)
        return redirect('index')
    try:
        urls = URL.objects.filter(
            user=request.user, archived=True).order_by('-id')
        data = Article.objects.filter(url__in=urls).select_related('url')
        paginator = Paginator(data, settings.URLS_PER_PAGE)
        page_number = request.GET.get('page')
        data = paginator.get_page(page_number)
    except:
        urls = []
    context = {'data': data}
    return render(request, 'archive.html', context)


@login_required
def delete(request, url_id):
    URL.objects.filter(id=url_id, user=request.user).delete()
    return redirect('archive')
