from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
from .form import ApiForm
from .models import Api
from project.models import Module


# Create your views here.
def list(request):

    if request.method == 'GET':
        context = {'type': 'list'}
        return render(request, 'case.html', context)
    else:
        return HttpResponse("404")


def debug(request):

    if request.method == 'GET':
        form = ApiForm
        content = {'form': form, 'type': 'debug'}
        return render(request, 'debug.html', content)
    else:
        return HttpResponse('404')


def debugging(request):
    if request.method == 'POST':
        url = request.POST.get('req_url')
        method = request.POST.get('req_method')
        header = request.POST.get('req_header')
        parameter = request.POST.get('req_parameter')
        type = request.POST.get('req_type')
        # 将paramter有String转成字典格式, 将单引号 ' 替换成 "
        parameter = json.loads(parameter.replace("'", "\""))

        # 使用requests发送请求
        if method.upper() == 'GET':
            res = requests.get(url=url, data=parameter, headers=header)

        if method.upper() == 'POST':
            # 区分form格式和json格式
            if type.upper() == 'FORM':
                res = requests.post(url, data=parameter, headers=header)
            else:
                res = requests.post(url, json=parameter, headers=header)
        print(res.text)
        return HttpResponse(res.text)

    else:
        content = {'type': 'debug'}
        return render(request, 'debug.html', content)


def update(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        url = request.POST.get('req_url')
        method = request.POST.get('req_method')
        header = request.POST.get('header')
        parameter = request.POST.get('req_parameter')
        type = request.POST.get('req_type')
        # 将paramter有String转成字典格式, 将单引号 ' 替换成 "
        parameter = json.loads(parameter.replace("'", "\""))
        module_id = request.POST.get("module")
        print(module_id)

        if url == '' or method == '' or type == '' or module_id == '':
            return HttpResponse('缺少关键参数!')

        if parameter == '':
            parameter = {}

        if header == '':
            header = '{}'


        # 查出module对象
        module = Module.objects.get(id=module_id)
        api = Api.objects.create(name=name, module=module,url=url,method=method,
                                        type=type, parameter=parameter,header=header)
        if api is not None:
            return HttpResponse('保存成功')
        else:
            return HttpResponse('保存失败')
    else:
        return HttpResponse('请求方法错误')
