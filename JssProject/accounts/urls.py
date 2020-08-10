from django.urls import path
from .views import signup, MyLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"), #이미 만들어진 클래스를 쓰려면 .as_View 를 사용해야한다. 
    # url표시, views에서 불러올 함수, 고유 이름 정해주기 

]