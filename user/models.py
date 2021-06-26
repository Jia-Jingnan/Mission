from django.db import models


# Create your models here.
# 表名 user_project
class Project(models.Model):
    # 会自动添加自增长的id
    name = models.CharField('项目名称', max_length=100, blank=False, default="")
    describe = models.TextField('项目描述', default='')
    status = models.BooleanField('项目状态', default=True)
    create_time = models.DateTimeField('创建时间', auto_now=True)

    # 重写toString方法
    def __str__(self):
        return self.name


class Module(models.Model):
    # 项目模块表
    # 项目与模块对应关系为一对多
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # 项目删除时，项目下的模块也一起删除
    name = models.CharField('模块名称', max_length=100, blank=False, default='')
    describe = models.TextField('模块描述', default='')
    # 自动添加创建时间
    create_time = models.DateTimeField('创建时间', auto_now=True)

    # 重写toString方法
    def __str__(self):
        return self.name
