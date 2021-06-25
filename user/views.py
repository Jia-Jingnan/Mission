from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth


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
            if user is not None:
                # auth.login(request,user) 记录用户登陆状态
                return render(request, 'project.html')

            else:
                return render(request, 'login.html', context)
