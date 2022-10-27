import requests

from bs4 import BeautifulSoup
from django.conf import settings


def sanitize_img_size(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    for img in soup.find_all('img'):
        img['width'] = '100%'
        img['height'] = 'auto'
    return str(soup)


def get_content(url: str):
    if settings.READABILITY_HOST:
        url = settings.READABILITY_HOST.rstrip(
            '/') + '/api/content/v1/parser?url=' + url
        try:
            return requests.get(url).json()
        except KeyError:
            return None
