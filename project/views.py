from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project.models import Project
from project.form import ProjectForm

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
    context = {
        'user': username,
        'projects': project_list,
        'project_recent': project_recent,
        'type': 'list',
    }
    return render(request, 'project_manage.html', context)


@login_required # 判断用户是否登陆
def add(request):
    if request.method == 'GET':
        form = ProjectForm()
        # 上下文
        context = {
            'type': 'add',
            'form': form
        }

    elif request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # 插入项目信息到project表
            # 获取表单信息
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']

            Project.objects.create(name=name, describe=describe)
            context = {
                'type': 'add',
                'form': form
            }
            return HttpResponseRedirect('/project/list/', context)

    else:
        form = ProjectForm()

    return render(request, 'project_manage.html', context)


def edit(request):
    # 获取要编辑的项目的id
    pass


def delete(request):
    pass