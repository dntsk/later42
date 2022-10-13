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
from django.contrib.auth.views import LoginView

from rest_framework import routers, serializers, viewsets

from later42.forms import CustomLoginForm
from later42.views import index, profile, api, api_token, signup, about


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
    path("accounts/login/", LoginView.as_view(authentication_form=CustomLoginForm), name="login"),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('profile/', profile.get, name='profile'),
    path('api/url/', api.URL.as_view(), name='urls'),
    path('delete/<int:url_id>', index.delete, name='delete'),
    path('api_token/', api_token.create, name='api_token'),
    path('', index.get, name='index'),
    path('about/', about.get, name='about'),
]
