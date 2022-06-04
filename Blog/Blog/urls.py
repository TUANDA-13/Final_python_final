"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',BASE,name='base'),
    path('login/',Login.as_view(),name='login'),
    path('',INDEX,name='home'),
    path('register/',Register.as_view(),name='register'),
    # path('single/',Single.as_view(),name='single'),
    path('blog/<int:pk>',Single.as_view(),name='blog'),
    path('addPost/',AddPost.as_view(),name='add_post'),
    path('addTopic/',AddTopic.as_view(),name='add_topic'),
    path('addUser/',AddUser.as_view(),name='add_user'),
    path('logout/',LOGOUT,name='logout'),
    path('mtopic/',ManageTopic.as_view(),name="manage_topic"),
    path('mpost/',ManagePost.as_view(),name="manage_post"),
    path('muser/',ManageUser.as_view(),name="manage_user"),
    path('topic/<int:pk>/',TopicView.as_view(),name='topic'),
    path('topic/<int:pk>/<int:page>/',TopicView.as_view(),name='topic'),
]