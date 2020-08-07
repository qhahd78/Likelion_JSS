from django.db import models

# Create your models here.
#자소설 틀을 만들어 놓는다. 글자수를 제한해놓고, 자소설 입력시 날짜와 시간을 표기하고 등등. 

class Jasoseol(models.Model):  #자소설 모델 만들기. 모델은 데이터베이스에 저장된다. models는 장고 모델이라는 것을 의미 
    title = models.CharField(max_length=50) # CharField. 글자수가 제한된 필드를 만들 때 사용한다. 
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True) # 날짜와 시간. 
