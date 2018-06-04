from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from .models import *
# Create your views here.

def index_views(request):
    return render(request,'index.html')

def login_views(request):
    # login-tag = '<a href="/login">登　录</a>'
    # logout-tag = '<a href="/registe">注册</a>'
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        msg='' 
        name = request.POST.get('uname')
        # password = make_password(request.POST.get('upwd'))
        password = request.POST.get('upwd')
        print(password)
        if not name or not password:
            msg='空用户名密码非法'
            return render(request,'login.html',locals())
        else:
            user = User.objects.filter(name=name)
            if user:
                if password == user[0].pwd:
                    return HttpResponseRedirect('/')
                else:
                    msg = '密码错误'
                    return render(request,'login.html',locals())
            else:
                msg = '无此用户'
                return render(request,'login.html',locals())


def registe_views(request):
    pw = make_password('123')
    return render(request,'registe.html',locals())


