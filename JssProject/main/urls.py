from django.urls import path
from .views import index, create, detail, delete, update, my_index, create_comment, delete_comment

urlpatterns = [
    # url표시, views에서 불러올 함수, 고유 이름 정해주기 
    path('', index, name='index'),
    path('my_jss',my_index,name="my_index"),
    path('create/',create, name='create'),
    path('detail/<int:jss_id>',detail, name='detail'), #id 도 같이 가지고 온다. 
    path('delete/<int:jss_id>',delete, name='delete'),
    path('update/<int:jss_id>',update, name='update'),
    
    #comment
    path('create_comment/<int:jss_id>/',create_comment, name='create_comment'),
    path('delete_comment/<int:jss_id>/<int:comment_id>/', delete_comment, name='delete_comment'),
]