import requests

from rest_framework.response import Response
from rest_framework.views import APIView
from bs4 import BeautifulSoup
from later42.models.urls import URL as URLModel
from django.conf import settings


class URL(APIView):
    def get_title(self, url: str):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('title').text
            return title
        except AttributeError:
            return None

    def get_content(self, url: str):
        url = settings.READABILITY_HOST.rstrip(
            '/') + '/api/content/v1/parser?url=' + url
        try:
            response = requests.get(url).json()
            return response['excerpt']
        except AttributeError:
            return None

    def post(self, request, format=None):
        url = request.GET.get('url')
        if url:
            title = self.get_title(url)
            if title is None:
                title = url

            content = None
            if settings.READABILITY_HOST:
                content = self.get_content(url)

            url = URLModel(url=url, user=request.user,
                           title=title, content=content)
            url.save()
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
