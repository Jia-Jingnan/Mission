from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project.models import Project

# Create your views here.


@login_required # 判断用户是否登陆
def list(request):
    # username = request.COOKIES.get('user')
    username = request.session.get('user')
    # 查询所有项目
    project_list = Project.objects.all()
    print(project_list)

    # 查询最近项目
    project_recent = Project.objects.filter(id__lt=5)
    print(project_recent)

    # 上下文
    context = {'user': username, 'projects': project_list, 'project_recent': project_recent}
    return render(request, 'project_manage.html', context)


def add(request):
    pass


def edit(request):
    pass


def delete(request):
    pass