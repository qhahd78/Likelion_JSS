from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#자소설 틀을 만들어 놓는다. 글자수를 제한해놓고, 자소설 입력시 날짜와 시간을 표기하고 등등. 

class Jasoseol(models.Model):  #자소설 모델 만들기. 모델은 데이터베이스에 저장된다. models는 장고 모델이라는 것을 의미 
    title = models.CharField(max_length=50) # CharField. 글자수가 제한된 필드를 만들 때 사용한다. 
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True) # 날짜와 시간. 
    author = models. ForeignKey(User, on_delete=models.CASCADE) #자소설이 지워지면, foreign 키도 지워진다 ? ? , null= True : 빈값을 허용한다. (작성자라는 필드가 있지만, 없어도 된다.)
#User 모델의 pk 키를 ForeignKey 로 저장해주고. 이 값을 author에 저장. 
#models.CASCADE 뜻은, 모델이 없어지면 객체 값도 다 사라진다. (User 모델이 사라지면, 연결되어있는 자소설도 모두 사라진다. )


#on_delete는 참조된 객체가 삭제될 때 어떤 동작을 할지 지정하는 옵션이다 .


# CASCADE: 하위 개체도 함께 삭제
# PROTECT: 참조된 개체의 삭제를 금지
# RESTRICT: PROTECT와 같이 삭제를 금지하지만 참조된 개체 안에 참조 개체가 있는 경우 하위 참조 개체의 on_delete 속성을 따라감
# SET_NULL: NULL 값으로 변경 (null 옵션이 True 값이어야 함)
# SET_DEFAULT: 설정해둔 default 값으로 변경 (default 옵션에 값이 있어야 함)
# SET(): 지정한 값으로 변경
# DO_NOTHING: 아무 동작도 하지 않음
