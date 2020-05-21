"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('news/', include('news.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
# include()는 다른 urlconfig를 참조할 수있게 해줌
# parsing된 url중에서 news, polls, admin을 잡아내서 우리가 만든 url파일로 연결을 시켜준다.
