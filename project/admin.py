from django.contrib import admin

from project.models import Project, Module


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'describe', 'status', 'create_time']


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'describe', 'project', 'create_time']

# 将自定义的两个类Project和Module也放到django的后台管理，做增加和删除修改等操作
# 映射到后台,注册到后台
admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)
