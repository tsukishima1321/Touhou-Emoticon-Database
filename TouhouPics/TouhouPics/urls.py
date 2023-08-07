from django.urls import path, re_path
from django.conf.urls import url
 
from . import views
 
urlpatterns = [
    re_path('^random/$', views.random),
    re_path('.',views.singlePic),
]