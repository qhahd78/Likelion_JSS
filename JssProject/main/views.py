from django.shortcuts import render, redirect
from .forms import JssForm
from .models import Jasoseol

# Create your views here.

def index(request): 
    all_jss = Jasoseol.objects.all() #all_jss에다가 모든 오브젝트를 넣어 보낸다 .
    return render(request, 'index.html', {'all_jss':all_jss}) 


def create(request): 
    if request.method == "POST" : 
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index') #렌더는 데이터 넘기기, 리다이렉트는 그냥 옮겨가는것.
    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form':jss_form})
    