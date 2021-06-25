from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.s
def index(request):
    return render(request, 'index.html')


def login(request):
    context = {'error': '用户名或密码错误'}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username == '' or password == '':
            return render(request, 'login.html', context)

        else:
            user = auth.authenticate(username=username, password=password)
            # context = {'user': user}
            if user is not None:
                auth.login(request,user) # 记录用户登陆状态
                # return render(request, 'project.html', context)
                # response = HttpResponseRedirect('/project_manage/')
                # response.set_cookie('user', username, 3600) # 添加浏览器cookie
                request.session['user'] = username
                return HttpResponseRedirect('/project_manage/')
            else:
                return render(request, 'index.html', context)


@login_required # 判断用户是否登陆
def project_manage(request):
    # username = request.COOKIES.get('user')
    username = request.session.get('user')
    context = {'user': username}
    return render(request, 'project_manage.html', context)


def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response