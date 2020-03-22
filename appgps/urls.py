from django.contrib import admin
from django.urls import path, re_path, include

from . import views

app_name = 'appgps'

urlpatterns = [
    
    re_path('^$', views.all_appgps, name="all"),
    re_path('^addnew/$', views.addnew_attraction, name="addnew"),      
]
