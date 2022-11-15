from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.validators import URLValidator
from later42.models.urls import URL as URLModel
from later42.tasks import get_url_content_task
from django.conf import settings


def validate_url(to_validate:str) -> bool:
    validator = URLValidator()
    try:
        validator(to_validate)
        return True
    except ValidationError as exception:
        return False


class URL(APIView):
    def post(self, request, format=None):
        if validate_url(request.GET.get('url')):
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
