"""JssProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from main.views import index, create, detail, delete, update #views에서 불러오는 함수들. 


urlpatterns = [
    # url표시, views에서 불러올 함수, 고유 이름 정해주기 
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('accounts.urls')),
]
