# Author:   jingnan
# Date:    2021/6/27
# Desc:
from django.urls import path
from project import views


urlpatterns = [
    path('list/', views.list),
    path('add/', views.add),
    path('edit/<int:pid>', views.edit),
    # path('/add', views.add),
]