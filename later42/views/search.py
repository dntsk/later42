"""Search view."""
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from later42.models.article import Article


@login_required
def search(request):
    """Search view."""
    pattern = request.POST.get("search")
    context = {}
    if request.method == "GET":
        return render(request, "search.html", context)
    elif request.method == "POST":
        data = Article.objects.filter(
            Q(title__contains=pattern)
            | Q(content__contains=pattern)
            | Q(short__contains=pattern)
            | Q(url__url__contains=pattern),
            url__user_id=request.user.id,
        ).select_related("url")
        paginator = Paginator(data, settings.URLS_PER_PAGE)
        page_number = request.GET.get("page")
        data = paginator.get_page(page_number)
        context = {"data": data}
        return render(request, "search.html", context)
