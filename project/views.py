from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project.models import Project, Module
from project.form import ProjectForm, ModuleForm

# Create your views here.

# 包含project和module的视图函数

# project视图函数
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
    return render(request, 'project.html', context)

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
            status = form.cleaned_data['status']

            Project.objects.create(name=name, describe=describe, status=status)
            context = {
                'type': 'add',
                'form': form
            }
            return HttpResponseRedirect('/project/list/', context)

    else:
        form = ProjectForm()

    return render(request, 'project.html', context)

@login_required
def edit(request, pid):

    # 获取要编辑的项目的id
    print(pid)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # 查询原数据
            project = Project.objects.get(id=pid)
            # 从表单中获取新的数据
            project.name = form.cleaned_data['name']
            project.describe = form.cleaned_data['describe']
            project.status = form.cleaned_data['status']
            project.save()
            return HttpResponseRedirect('/project/list/')
    else:
        if pid:
            form = ProjectForm(
                instance = Project.objects.get(id=pid)
            )
    context = {
        'type': 'edit',
        'form': form,
        'pid': pid
    }

    return render(request, 'project.html', context)

@login_required
def delete(request, pid):
    # 查询出数据,并执行删除操作
    Project.objects.get(id=pid).delete()
    # 重定向至列表页面
    return HttpResponseRedirect('/project/list/')



# module视图函数
@login_required # 判断用户是否登陆
def module_list(request):
    # username = request.COOKIES.get('user')
    username = request.session.get('user')
    # 查询所有项目
    module_list = Module.objects.all()
    print(module_list)

    # 上下文
    context = {
        'user': username,
        'modules': module_list,
        'type': 'list',
    }
    return render(request, 'module.html', context)


@login_required # 判断用户是否登陆
def module_add(request):
    if request.method == 'GET':
        form = ModuleForm()
        # 上下文
        context = {
            'type': 'add',
            'module_form': form
        }

    elif request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            # 插入项目信息到project表
            # 获取表单信息
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            project = form.cleaned_data['project']

            Module.objects.create(name=name, describe=describe, project=project)
            context = {
                'type': 'add',
                'module_form': form
            }
            return HttpResponseRedirect('/project/module/list/', context)

    else:
        form = ModuleForm()

    return render(request, 'module.html', context)


@login_required
def module_edit(request, mid):

    # 获取要编辑的项目的id
    print(mid)
    if request.method == 'POST':
        print(request.method)
        form = ModuleForm(request.POST)
        if form.is_valid():
            # 查询原数据
            module = Module.objects.get(id=mid)
            # 从表单中获取新的数据
            module.name = form.cleaned_data['name']
            module.describe = form.cleaned_data['describe']
            module.project = form.cleaned_data['project']
            module.save()
            return HttpResponseRedirect('/project/module/list/')
    else:
        if mid:
            form = ModuleForm(
                instance = Module.objects.get(id=mid)
            )
    context = {
        'type': 'edit',
        'module_form': form,
        'mid': mid
    }

    return render(request, 'module.html', context)


@login_required
def module_delete(request, mid):
    # 查询出数据,并执行删除操作
    Module.objects.get(id=mid).delete()
    # 重定向至列表页面
    return HttpResponseRedirect('/project/module/list/')
