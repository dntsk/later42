from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from later42.models.urls import URL


def get(request):
    try:
        urls = URL.objects.filter(user=request.user).order_by('-id')
        context = {'urls': urls}
    except:
        context = {'urls': []}
    return render(request, 'index.html', context)


@login_required
def delete(request, url_id):
    URL.objects.filter(id=url_id, user=request.user).delete()
    return redirect('index')
