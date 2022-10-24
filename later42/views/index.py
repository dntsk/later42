from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from later42.models.urls import URL


def get(request):
    try:
        urls = URL.objects.filter(
            user=request.user, archived=False).order_by('-id')
    except:
        urls = []
    context = {'urls': urls}
    return render(request, 'index.html', context)


@login_required
def archive(request, url_id=None):
    if url_id:
        URL.objects.filter(id=url_id, user=request.user).update(archived=True)
        return redirect('index')
    try:
        urls = URL.objects.filter(
            user=request.user, archived=True).order_by('-id')
    except:
        urls = []
    context = {'urls': urls}
    return render(request, 'archive.html', context)


@login_required
def delete(request, url_id):
    URL.objects.filter(id=url_id, user=request.user).delete()
    return redirect('archive')
