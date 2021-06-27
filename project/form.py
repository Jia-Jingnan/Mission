# Author:   jingnan
# Date:    2021/6/27
# Desc:     处理form表单的模块
from django import forms
from project.models import Project


# class ProjectForm(forms.Form):
#     name = forms.CharField(label='项目名称', max_length=100)
#     describe = forms.CharField(label='项目描述', widget=forms.Textarea)
#     status = forms.BooleanField(label='状态')

class ProjectForm(forms.ModelForm):
    # form展示的字段
    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']
