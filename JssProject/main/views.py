from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm
from .models import Jasoseol
from django.http import Http404
# Create your views here.

def index(request): 
    all_jss = Jasoseol.objects.all() #all_jss에다가 모든 오브젝트를 넣어 보낸다 .
    return render(request, 'index.html', {'all_jss':all_jss}) 


def create(request): 
    if request.method == "POST" : 
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index') # 렌더는 데이터 넘기기, 리다이렉트는 그냥 옮겨가는것.
    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form':jss_form})
    
def detail(request, jss_id) : # 함수내에서 인자로써 id 도 같이 받아올 수 있다. 
    # try: 
    #    my_jss = Jasoseol.objects.get(pk=jss_id) # my_jss 에 Jasoseol 오브젝트에서 한 개만 가지고 온다. 
    # except: 
    #    raise Http404

    my_jss = get_object_or_404(Jasoseol, pk=jss_id) #모델 쓰고, id 쓰면 됨 
    
    
    return render (request,'detail.html', {'my_jss': my_jss} )

def delete(request, jss_id) : 
    my_jss = Jasoseol.objects.get(pk=jss_id)
    my_jss.delete()

    return redirect('index')

def update(request, jss_id): 
    my_jss = Jasoseol.objects.get(pk=jss_id) #원하는 오브젝트를 가져온다 .
    jss_form = JssForm(instance=my_jss) #모델 폼을 jss_form에 담아준다. 특정 오브젝트를 instance라는 인자에 넣어준다. 모델폼에 특정 오브젝트가 담긴다. 
    if request.method == "POST": 
        updated_form = JssForm(request.POST, instance=my_jss)#유효성 검증
        if updated_form.is_valid(): #검증을 통과했을 경우 
            updated_form.save() #세이브 해준다. 
            return redirect('index')
    
    return render(request, 'create.html', {'jss_form' : jss_form}) #수정을 누르면 create 창으로 넘어가게 . 