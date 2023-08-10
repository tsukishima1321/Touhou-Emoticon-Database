from django.urls import path, re_path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
 
from . import views
 
urlpatterns = [
    re_path('^api/$',views.api),
    re_path('^random/$', views.random),
    re_path('^randoms/$', views.randoms),
    re_path('^search/$', views.search),
    re_path('.',views.singlePic),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)