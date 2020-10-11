from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .form import LoginForm

# Create your views here.
def login_handle(request):
    
    if request.method == 'GET':   # 获取登录页面
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form': login_form})
    
    if request.method == 'POST':  # 登录验证
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            form_data = login_form.cleaned_data
            user = authenticate(username=form_data['username'], password=form_data['password'])
            if user: 
                # 验证成功
                login(request, user)
                # 进入首页
                return render(request, 'index.html')
            else:
                # 验证失败
                return HttpResponse('用户名密码错误')
        
        return HttpResponse('Unkown Exception')
