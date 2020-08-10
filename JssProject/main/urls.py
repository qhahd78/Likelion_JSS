from django.urls import path
from .views import index, create, detail, delete, update 

urlpatterns = [
    # url표시, views에서 불러올 함수, 고유 이름 정해주기 
    path('', index, name='index'),
    path('create/',create, name='create'),
    path('detail/<int:jss_id>',detail, name='detail'), #id 도 같이 가지고 온다. 
    path('delete/<int:jss_id>',delete, name='delete'),
    path('update/<int:jss_id>',update, name='update'),
]