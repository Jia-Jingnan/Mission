# Author:   jingnan
# Date:    2021/6/27
# Desc:
from django.urls import path
from api import views


urlpatterns = [

    # case urls
    path('list/', views.list),
    path('debug/', views.debug),
    path('debugging/', views.debugging),
    # 保存或更新接口
    path('update/', views.update),
    # path('edit/<int:pid>/', views.edit),
    # path('delete/<int:pid>/', views.delete),
]