from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView #장고 내장 함수. 불러와서 클래스로 상속 받은 후에 클래스를 수정하면 오버라이딩 된다고 함. 

# Create your views here.

def signup(request): 
    regi_form = UserCreationForm()
    if request.method == "POST": 
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')

    return render(request, 'signup.html', {'regi_form':regi_form})

class MyLoginView(LoginView): # myloginview 가 loginview의 특성을 다 가져왔음. 
    template_name = 'login.html'
