"""mission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views
import project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('accounts/login/', views.index),
    path('login/', views.login),
    # path('project_manage/', views.project_manage),
    path('logout/', views.logout),

    # project app urls
    path('project/', include('project.urls')),

    # api app urls， include api and case
    path('api/', include('api.urls')),

]
