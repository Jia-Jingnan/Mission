from django.contrib import admin
from api.models import Api


# Register your models here.

class ApiAdmin(admin.ModelAdmin):
    list_display = ['module', 'name', 'url', 'method', 'type', 'header', 'parameter', 'asserts']


# 将自定义的两个类Project和Module也放到django的后台管理，做增加和删除修改等操作
# 映射到后台,注册到后台
admin.site.register(Api, ApiAdmin)


