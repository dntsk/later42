from rest_framework.response import Response
from rest_framework.views import APIView
from later42.libs.content import get_content
from later42.models.urls import URL as URLModel
from later42.tasks import get_url_content_task
from django.conf import settings


class URL(APIView):
    def post(self, request, format=None):
        if request.GET.get('url'):
            get_url_content_task.delay(request.GET.get('url'), request.user.id)
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
