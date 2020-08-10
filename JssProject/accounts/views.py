from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView #장고 내장 함수. 불러와서 클래스로 상속 받은 후에 클래스를 수정하면 오버라이딩 된다고 함. 

# Create your views here.

def signup(request): 
    regi_form = UserCreationForm() #객체이름 = 클래스이름() 객체가 클래스의 특성을 받음.
    if request.method == "POST": # 전달 받은 게 없으면 
        filled_form = UserCreationForm(request.POST) # 전달 받은 게 있으면 filled_form에 저장 
        if filled_form.is_valid(): # 받은 값이 유효한가? 
            filled_form.save() # 서버(db)에 저장한다. (admin 홈페이지)
            return redirect('index') # index(urls 에서 name=index)를 불러온다. 
        else : 
            pass
    return render(request, 'signup.html', {'regi_form':regi_form}) #regi_form에 넣어서 html로 전달

class MyLoginView(LoginView): # myloginview 가 loginview의 특성을 다 가져왔음. 
    template_name = 'registration/login.html' # template_name 이라는 값을 변경한다. login.html 로. 

#views.py 에서는 def를 이용하거나, class를 이용한다. 
#views 함수의 request는 submit 버튼을 통해 form내용의 input 타입의 값이 전해진 값