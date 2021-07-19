from django.db import models
from project.models import Project, Module

# Create your models here.
# 表名 user_project
class Api(models.Model):
    # 会自动添加自增长的id
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField('接口名称', max_length=100, blank=False, default="")
    url = models.CharField('接口地址', max_length=100, default="")
    method = models.CharField('请求方式', max_length=100, default="")
    type = models.CharField('请求数据类型', max_length=100, default='form')
    header = models.TextField('请求头', default="")
    parameter = models.TextField('请求参数', default="")
    asserts = models.TextField('断言', default="")
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    # 重写toString方法
    def __str__(self):
        return self.name

    # 自定义表名
    class Meta:
        db_table = 'api'
