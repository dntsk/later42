"""later42 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from django.contrib.auth.models import User
# from django.contrib.auth import views

from rest_framework import routers, serializers, viewsets

# from later42.forms import CustomLoginForm
from later42.views import account_activation, index, profile, api, api_token, reader, signup, about


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup.register, name='signup'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         account_activation.activate, name='activate'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', profile.get, name='profile'),
    path('api/url/', api.URL.as_view(), name='urls'),
    path('delete/<int:url_id>', index.delete, name='delete'),
    path('api_token/', api_token.create, name='api_token'),
    path('', index.get, name='index'),
    path('about/', about.get, name='about'),
    path('archive/', index.archive, name='archive'),
    path('archive/<int:url_id>', index.archive, name='archive_url'),
    path('reader/<int:url_id>', reader.get, name='reader'),
]
