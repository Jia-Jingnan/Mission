# Author:   jingnan
# Date:    2021/7/21
# Desc:
from django import forms
from .models import Api


class ApiForm(forms.ModelForm):

    class Meta:
        model = Api
        fields = ['module']