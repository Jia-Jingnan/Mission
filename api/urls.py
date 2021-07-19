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
    # path('edit/<int:pid>/', views.edit),
    # path('delete/<int:pid>/', views.delete),
]