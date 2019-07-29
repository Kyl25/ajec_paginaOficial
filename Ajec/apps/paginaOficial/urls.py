from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from apps.paginaOficial.views import *


app_name="ajec" 
urlpatterns = [
    url(r'^home/$',home.as_view(),name="home"),
    url(r'^inicio/$',(inicio),name="inicio"),
    url(r'^$',index),
    
]
