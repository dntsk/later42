from rest_framework.response import Response
from rest_framework.views import APIView
from later42.libs.content import get_content
from later42.models.urls import URL as URLModel
from later42.tasks import get_url_content_task
from django.conf import settings


class URL(APIView):
    def post(self, request, format=None):
        url = request.GET.get('url')
        if url:
            page = get_content(url)

            try:
                title = page['title']
            except KeyError:
                title = ''

            content = None
            if settings.READABILITY_HOST:
                try:
                    content = page['excerpt']
                except KeyError:
                    content = ''

            url = URLModel(url=url, user=request.user,
                           title=title, content=content)
            url.save()
            get_url_content_task.delay(url.id)
            return Response({'status': 'success'})
        else:
            return Response({'status': 'error'})

    def delete(self, request, format=None):
        id = request.GET.get('id')
        if id:
            url = URLModel.objects.filter(id=id).first()
            if url:
                url.archived = True
                url.save()
            return Response({'status': 'success'})
        else:
            return Response({'status': 'error'})
