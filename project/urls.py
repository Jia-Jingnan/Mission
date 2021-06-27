# Author:   jingnan
# Date:    2021/6/27
# Desc:
from django.urls import path
from project import views


urlpatterns = [

    # project urls
    path('list/', views.list),
    path('add/', views.add),
    path('edit/<int:pid>/', views.edit),
    path('delete/<int:pid>/', views.delete),

    # module urls
    path('module/list/', views.module_list),
    path('module/add/', views.module_add),
    path('module/edit/<int:mid>/', views.module_edit),
    path('module/delete/<int:mid>/', views.module_delete),
]