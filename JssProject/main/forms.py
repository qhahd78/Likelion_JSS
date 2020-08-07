from django import forms #모델폼 불러오기 위해 
from .models import Jasoseol 

class JssForm(forms.ModelForm): #모델폼을 상속 

    class Meta: #메타에 2가지 인자 넣음 
        model = Jasoseol
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs): #클래스 내의 내장 함수. 
        super().__init__(*args, **kwargs) #모든 것을 받아들이는 인자가 args, kwargs.  
        self.fields['title'].label = "제목"
        self.fields['content'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({
            'class': 'jss_title',
            'placeholder': '제목',
        })
