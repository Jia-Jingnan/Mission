from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json


# Create your views here.
def list(request):

    if request.method == 'GET':
        context = {'type': 'list'}
        return render(request, 'case.html', context)
    else:
        return HttpResponse("404")


def debug(request):

    if request.method == 'GET':
        content = {'type': 'debug'}
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
            res = requests.get(url, parameter, header)

        if method.upper() == 'POST':
            # 区分form格式和json格式
            if type.upper() == 'FORM':
                res = requests.post(url, data=parameter, headers=header)
            else:
                res = requests.post(url, json=parameter, headers=header)

        return HttpResponse(res.text)

    else:
        content = {'type': 'debug'}
        return render(request, 'debug.html', content)
