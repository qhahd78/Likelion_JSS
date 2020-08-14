from django import forms #모델폼 불러오기 위해 
from .models import Jasoseol, Comment

class JssForm(forms.ModelForm): #모델폼을 상속 

    class Meta: #메타에 2가지 인자 넣음 
        model = Jasoseol #어떤 모델 쓸건지 . Jasoseol 모델을 쓸거다 ! 
        fields = ('title', 'content',) #author 추가하면 자소서 생성 페이지에 Author 항목 추가

    def __init__(self, *args, **kwargs): #클래스 내의 내장 함수. # 오버라이딩 !!!!!! ( 이미 있는 거 가져와서 쓰는거 )
        super().__init__(*args, **kwargs) #모든 것을 받아들이는 인자가 args, kwargs.  
        self.fields['title'].label = "제목" #라벨 값을 바꿔준다. '제목' 이랑 '자기소개서 내용' 이라고 바꿔줌. 
        self.fields['content'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({ # 바꾸는 거 x, 추가를 해주는 것이다. 
            'class': 'jss_title', #class=jss_title 랑 placeholder='제목'를 만들어준다. 
            'placeholder': '제목',
        })

class CommentForm(forms.ModelForm):

    class Meta: 
        model = Comment #폼과 연결될 모델 
        fields = ('content',)
