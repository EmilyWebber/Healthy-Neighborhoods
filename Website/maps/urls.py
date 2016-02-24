from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^hello/$', views.hello),
    url(r'(?i)healthy.*neighborhood', views.healthy_neighborhoods),
    url('', views.blank),
]