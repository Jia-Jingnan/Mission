from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
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
            return render(request, 'index.html', context)

        else:
            user = auth.authenticate(username=username, password=password)
            # context = {'user': user}
            if user is not None:
                auth.login(request,user) # 记录用户登陆状态
                request.session['user'] = username
                return HttpResponseRedirect('/project/list/')
            else:
                return render(request, 'index.html', context)

    else:
        return render(request, 'index.html', context)





def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response