# views 에서 변수를 지정해서 templates에서 사용할 수 있는 것. 변수는 무조건 views에서 온다. 

from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm, CommentForm #같은 위치에 있는 forms에서 JssForm 클래스를 불러온다. 
from .models import Jasoseol, Comment #같은 위치에 있는 models에서 Jasoseol 이라는 모델을 불러온다. 
from django.http import Http404 
from django.core.exceptions import PermissionDenied #PermissionDenied 불러오기/ 
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request): #request(요청)을 넘겨받아
    all_jss = Jasoseol.objects.all() #all_jss에다가 모든 오브젝트를 넣어 보낸다 .
    return render(request, 'index.html', {'all_jss':all_jss}) #render 라는 메소드를 호출한다. request 고정, 연결할 템플릿 경로, 딕셔너리 형태로 템플릿에 넘겨준다. 

def my_index(request) : 
    my_jss = Jasoseol.objects.filter(author=request.user) #오브젝트들 중에서, author 에서 현재 로그인된 유저가 들어있는 오브젝트만 가져오겠다. ??
    return render(request, 'index.html', {'all_jss':my_jss}) #render 라는 메소드를 호출한다. request 고정, 연결할 템플릿 경로, 딕셔너리 형태로 템플릿에 넘겨준다. 
#필터링 거친 my_jss를 all_jss(이미 있는 변수! 덮어쓴다고 생각.) 에다가 넣어서 index 에다가 다시 씁니다 !!!

#모델을 불러오는 방법 
# 모델.objects.all() - 해당 모델의 모든 객체 가져옴 
# 모델.objects.get(pk값 등등) -해당 모델의 특정 값 하나만.
# 모델.objectsfilter(같은 값이면) - 해당 조건에 해당하는 모든 값을 가져온다.
                         # - 검색하는 데에 많이 쓴대요 


#login_required 는 사용자가 로그인이 안 되어있으면 표시되어있는 url로 이동시켜준다. 
@login_required(login_url='/login') #사용하려면 원하는 함수에 붙혀주기, /login 페이지로 이동
def create(request): 
    # print(request.user) #현재 로그인한 유저를 알아보기 위해 프린트한다.
    # if not request.user.is_authenticated: #유저가 인증이 안 되어 있으면,
    #     return redirect('login')

    if request.method == "POST": # post는 정보의 형식을 말한다. (get post할 때 그 post임)
        filled_form = JssForm(request.POST)
        if filled_form.is_valid(): #유효성 검사 
            temp_form = filled_form.save(commit=False) #temp fomr에 filled form을 넣어준다. #commit False.는 세이브를 지연, 그 사이에 어떤 행위들을 넣어줄 수 있다 .
            temp_form.author = request.user # 현재 로그인된 유저를 넣어준다. 
            filled_form.save()
            return redirect('index') # 렌더는 데이터 넘기기, 리다이렉트는 그냥 옮겨가는것.
    jss_form = JssForm()

    return render(request, 'create.html', {'jss_form':jss_form})

@login_required(login_url='/login') 
def detail(request, jss_id) : # 함수내에서 인자로써 id 도 같이 받아올 수 있다. 
    # try: 
    #    my_jss = Jasoseol.objects.get(pk=jss_id) # my_jss 에 Jasoseol 오브젝트에서 한 개만 가지고 온다. 
    # except: 
    #    raise Http404

    my_jss = get_object_or_404(Jasoseol, pk=jss_id) #모델 쓰고, id 쓰면 됨 
    Comment_form = CommentForm() #Comment_form 이라는 변수에 CommentForm을 담는다. 폼을 담는다. ! 
    
    return render (request,'detail.html', {'my_jss': my_jss, 'comment_form': Comment_form})

def delete(request, jss_id) : 
    
    my_jss = Jasoseol.objects.get(pk=jss_id)
    if request.user == my_jss.author: #url 이용해서 삭제하는 것을 방지. user와 author(작성자)가 같으면
        my_jss.delete() # 자소서를 삭제시키고 
        return redirect('index') # 첫화면을 불러온다.

    raise PermissionDenied #(user와 작성자가 다른데 지우려고 하면)에러를 띄운다. 
#raise = 오류 띄울 때 씀. return = 어떤 값을 반환할 때 씀 !!
def update(request, jss_id): 
    my_jss = Jasoseol.objects.get(pk=jss_id) #원하는 오브젝트를 가져온다 .
    jss_form = JssForm(instance=my_jss) #모델 폼을 jss_form에 담아준다. 특정 오브젝트를 instance라는 인자에 넣어준다. 모델폼에 특정 오브젝트가 담긴다. 
    if request.method == "POST": 
        updated_form = JssForm(request.POST, instance=my_jss)#유효성 검증
        if updated_form.is_valid(): #검증을 통과했을 경우 
            updated_form.save() #세이브 해준다. 
            return redirect('index')
    
    return render(request, 'create.html', {'jss_form' : jss_form}) #수정을 누르면 create 창으로 넘어가게 . 

def create_comment(request, jss_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        temp_form = comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.jasoseol = Jasoseol.objects.get(pk=jss_id)
        temp_form.save()
        return redirect('detail', jss_id)

def delete_comment(request, jss_id , comment_id): 
    my_comment = Comment.objects.get(pk=comment_id)
    if request.user == my_comment.author: 
        my_comment.delete()
        return redirect('detail', jss_id)

    else: 
        raise PermissionDenied